import graphene as gr
from graphene import relay

from . import types, inputs
from ..helpers import (
    enforce_user_requirements,
    get_user_context,
    get_facilitator_license,
)
from ...models.users import actions as model_actions


class CreateMe(relay.ClientIDMutation):
    Input = inputs.NewUserFields

    ok = gr.Boolean()
    user = gr.Field(types.User)

    @classmethod
    @enforce_user_requirements(auth=True, no_user=True)
    def mutate_and_get_payload(cls, root, info, **params):
        token = info.context.current_user.jwt
        user = model_actions.UserBuilder.from_token(token, **params).create(
            info.context.session
        )
        return cls(ok=True, user=user)


class UpdateMe(relay.ClientIDMutation):
    Input = inputs.UserFields

    ok = gr.Boolean()
    user = gr.Field(types.User)

    @classmethod
    @enforce_user_requirements(auth=True, user=True)
    def mutate_and_get_payload(cls, root, info, **params):
        current_user = info.context.current_user.user
        model_actions.patch_user(current_user, **params)
        info.context.session.commit()
        return cls(ok=True, user=current_user)


class DeleteMe(relay.ClientIDMutation):
    ok = gr.Boolean()
    user_id = gr.GlobalID(parent_type=types.User)

    @classmethod
    @enforce_user_requirements(auth=True, user=True)
    def mutate_and_get_payload(cls, root, info):
        current_user = info.context.current_user.user
        user_id = current_user.id
        model_actions.delete_user(current_user)
        info.context.session.commit()
        return cls(ok=True, user_id=user_id)


class AddParticipantContext(relay.ClientIDMutation):
    Input = inputs.NewParticipantContextFields

    ok = gr.Boolean()
    participant_context = gr.Field(types.ParticipantContext)

    @classmethod
    @enforce_user_requirements(auth=True, user=True)
    def mutate_and_get_payload(cls, root, info, **params):
        current_user = info.context.current_user.user
        context = model_actions.create_participant_context(**params)
        current_user.contexts.append(context)
        info.context.session.commit()
        return cls(ok=True, participant_context=context)


class UpdateParticipantContext(relay.ClientIDMutation):
    Input = inputs.UpdateParticipantContextFields

    ok = gr.Boolean()
    participant_context = gr.Field(types.ParticipantContext)

    @classmethod
    @enforce_user_requirements(auth=True, user=True)
    def mutate_and_get_payload(cls, root, info, **params):
        context = get_user_context(
            info, params.pop("id"), only_type="ParticipantContext"
        )
        model_actions.patch_user_context(
            context, **params.get("participant_context")
        )

        info.context.session.commit()
        return cls(ok=True, participant_context=context)


class RemoveParticipantContext(relay.ClientIDMutation):
    class Input:
        id = gr.GlobalID()

    ok = gr.Boolean()
    participant_context_id = gr.GlobalID(parent_type=types.ParticipantContext)

    @classmethod
    @enforce_user_requirements(auth=True, user=True)
    def mutate_and_get_payload(cls, root, info, **params):
        participant_context = get_user_context(
            info, params.get("id"), only_type="ParticipantContext"
        )
        participant_context_id = participant_context.id
        model_actions.remove_user_context(participant_context)
        info.context.session.commit()
        return cls(ok=True, participant_context_id=participant_context_id)


class AddFacilitatorContext(relay.ClientIDMutation):
    Input = inputs.NewFacilitatorContextFields

    ok = gr.Boolean()
    facilitator_context = gr.Field(types.FacilitatorContext)

    @classmethod
    @enforce_user_requirements(auth=True, user=True)
    def mutate_and_get_payload(cls, root, info, **params):
        current_user = info.context.current_user.user
        context = model_actions.create_facilitator_context(**params)
        current_user.contexts.append(context)
        info.context.session.commit()
        return cls(ok=True, facilitator_context=context)


class UpdateFacilitatorContext(relay.ClientIDMutation):
    Input = inputs.UpdateFacilitatorContextFields

    ok = gr.Boolean()
    facilitator_context = gr.Field(types.FacilitatorContext)

    @classmethod
    @enforce_user_requirements(auth=True, user=True)
    def mutate_and_get_payload(cls, root, info, **params):
        context = get_user_context(
            info, params.pop("id"), only_type="FacilitatorContext"
        )
        model_actions.patch_user_context(
            context, **params.get("facilitator_context")
        )

        info.context.session.commit()
        return cls(ok=True, facilitator_context=context)


class RemoveFacilitatorContext(relay.ClientIDMutation):
    class Input:
        id = gr.GlobalID()

    ok = gr.Boolean()
    facilitator_context_id = gr.GlobalID(parent_type=types.FacilitatorContext)

    @classmethod
    @enforce_user_requirements(auth=True, user=True)
    def mutate_and_get_payload(cls, root, info, **params):
        facilitator_context = get_user_context(
            info, params.get("id"), only_type="FacilitatorContext"
        )
        facilitator_context_id = facilitator_context.id
        model_actions.remove_user_context(facilitator_context)
        info.context.session.commit()
        return cls(ok=True, facilitator_context_id=facilitator_context_id)


class AddFacilitatorLicense(relay.ClientIDMutation):
    class Input:
        facilitator_context_id = gr.GlobalID()
        facilitator_license = gr.Field(lambda: inputs.FacilitatorLicenseInput)

    ok = gr.Boolean()
    facilitator_license = gr.Field(types.FacilitatorLicense)

    @classmethod
    @enforce_user_requirements(auth=True, user=True)
    def mutate_and_get_payload(cls, root, info, **params):
        facilitator = get_user_context(
            info,
            params.get("facilitator_context_id"),
            only_type="FacilitatorContext",
        )
        facilitator_license = model_actions.create_facilitator_license(
            **params.get("facilitator_license")
        )
        facilitator.licenses.append(facilitator_license)
        info.context.session.commit()
        return cls(ok=True, facilitator_license=facilitator_license)


class RemoveFacilitatorLicense(relay.ClientIDMutation):
    class Input:
        facilitator_context_id = gr.GlobalID()
        facilitator_license_id = gr.GlobalID()

    ok = gr.Boolean()
    facilitator_license_id = gr.GlobalID(parent_type=types.FacilitatorLicense)

    @classmethod
    @enforce_user_requirements(auth=True, user=True)
    def mutate_and_get_payload(cls, root, info, **params):
        facilitator_license = get_facilitator_license(info, **params)
        facilitator_license_id = facilitator_license.id
        model_actions.remove_facilitator_license(facilitator_license)
        info.context.session.commit()
        return cls(ok=True, facilitator_license_id=facilitator_license_id)


class Mutation(gr.ObjectType):
    create_me = CreateMe.Field()
    update_me = UpdateMe.Field()
    delete_me = DeleteMe.Field()

    add_participant_context = AddParticipantContext.Field()
    update_participant_context = UpdateParticipantContext.Field()
    remove_participant_context = RemoveParticipantContext.Field()

    add_facilitator_context = AddFacilitatorContext.Field()
    update_facilitator_context = UpdateFacilitatorContext.Field()
    remove_facilitator_context = RemoveFacilitatorContext.Field()

    add_facilitator_license = AddFacilitatorLicense.Field()
    remove_facilitator_license = RemoveFacilitatorLicense.Field()
