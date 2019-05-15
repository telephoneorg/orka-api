from functools import partial

from graphql_relay import from_global_id, to_global_id as _to_global_id
from graphql import GraphQLError
from graphene import relay


def get_type(type_name=None):
    if type_name:
        from . import schema

        definition = schema.get_type(type_name)
        return definition.graphene_type


def lazy_get_type(type_name=None):
    return partial(get_type, type_name)


def id_from_globalid(global_id, verify_type=None):
    type_, id_ = from_global_id(global_id)
    if verify_type:
        assert type_ == verify_type
    return int(id_)


def to_global_id(type_name, id_):
    return _to_global_id(type_name, id_)


def unmask(**config):
    """Usage:
    @unmask(id=Room, property_id=Property)
    def resolve_room(root, info, id, property_id, **kwargs):
        return rooms_loader.load(
            {'context': info.context, 'id': int(property_id)}
        ).then(lambda rooms: [
            item for item in rooms if item.id == int(id)
        ][0])
    """

    def unmask_decorator(func):
        def unmask_wrapper(obj, info, **kwargs):
            for arg_name, class_name in config.items():
                if kwargs[arg_name]:
                    schema_type, unmasked_id = relay.Node.from_global_id(
                        kwargs[arg_name]
                    )

                    if schema_type != class_name:
                        kwargs[arg_name] = None

                    kwargs[arg_name] = unmasked_id
            return func(obj, info, **kwargs)

        return unmask_wrapper

    return unmask_decorator


def get_user_context(info, user_context_id, only_type=None):
    if only_type:
        only_type = get_type(only_type)
    user_context = relay.Node.get_node_from_global_id(
        info, user_context_id, only_type
    )
    if (
        not user_context
        or user_context.user_id != info.context.current_user.user.id
    ):
        raise GraphQLError("Invalid Context for User")
    return user_context


def get_facilitator_license(
    info, facilitator_license_id, facilitator_context_id=None
):
    license_type = get_type("FacilitatorLicense")
    license = relay.Node.get_node_from_global_id(
        info, facilitator_license_id, license_type
    )
    if not license or (
        facilitator_context_id
        and license.facilitator_context_id
        != id_from_globalid(facilitator_context_id)
    ):
        raise GraphQLError("Invalid License for Facilitator")
    return license


def get_info_from_args(args):
    for arg in args:
        if type(arg).__name__ == "ResolveInfo":
            return arg


class enforce_user_requirements:
    def __init__(self, auth=False, user=False, no_user=False):
        self.require_auth = auth
        self.require_user = user
        self.require_no_user = no_user

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            info = get_info_from_args(args)
            context = info.context
            current_user = context.current_user

            if self.require_auth and current_user.is_anonymous:
                raise GraphQLError("User not authenticated")

            user_in_db = current_user.is_in_database
            if self.require_user and not user_in_db:
                raise GraphQLError("User doesn't exist")
            if self.require_no_user and user_in_db:
                raise GraphQLError("User already exists")

            return func(*args, **kwargs)

        return wrapper
