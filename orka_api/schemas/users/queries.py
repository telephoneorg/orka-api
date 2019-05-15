import graphene as gr
from graphene import relay
from . import types
from ..helpers import enforce_user_requirements


class Query(gr.ObjectType):
    node = relay.Node.Field()
    me = gr.Field(types.User, required=True)
    profile = relay.Node.Field(types.Profile, required=True)

    @enforce_user_requirements(auth=True, user=True)
    def resolve_me(self, info):
        current_user = info.context.current_user
        return current_user.user
