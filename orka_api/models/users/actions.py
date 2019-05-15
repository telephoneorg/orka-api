from ..base.helpers import (
    recursive_patch,
    recursive_create,
    recursive_soft_delete,
)


def create_user(**params):
    return recursive_create("User", **params)


def patch_user(user, **params):
    return recursive_patch(user, params)


def delete_user(user):
    for user_context in user.contexts:
        recursive_soft_delete(user_context)
    return recursive_soft_delete(user)


def create_participant_context(**params):
    return recursive_create("ParticipantContext", **params)


def create_facilitator_context(**params):
    return recursive_create("FacilitatorContext", **params)


def patch_user_context(context, **params):
    return recursive_patch(context, params)


def remove_user_context(context):
    return recursive_soft_delete(context)


def create_facilitator_license(**params):
    return recursive_create("FacilitatorLicense", **params)


def remove_facilitator_license(license):
    return recursive_soft_delete(license)


def create_identity(**params):
    return recursive_create("Identity", **params)


class UserBuilder:
    def __init__(self, **params):
        self.user = create_user(**params)

    def set_email(self, email):
        self.user.email = email
        return self

    def add_identity(self, **params):
        self.user.identities.append(create_identity(**params))
        return self

    def create(self, session):
        session.add(self.user)
        session.commit()
        return self.user

    @classmethod
    def from_token(cls, token, **params):
        return (
            cls(**params)
            .set_email(token.get("email"))
            .add_identity(subject=token.get("sub"))
        )
