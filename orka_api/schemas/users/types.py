import graphene as gr
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from ... import models, constants


__all__ = [
    "User",
    "UserContext",
    "UserContextConnection",
    "ParticipantContext",
    "FacilitatorContext",
    "Profile",
    "Identity",
    "NotificationPolicy",
    "FacilitatorLicense",
]


class User(SQLAlchemyObjectType):
    class Meta:
        model = models.User
        interfaces = (relay.Node,)
        exclude_fields = ("deleted", "financial_details")

    contexts = relay.ConnectionField(lambda: UserContextConnection)


class UserContext(gr.Interface):
    id = gr.GlobalID(required=True)
    type = gr.Field(gr.Enum.from_enum(constants.UserContextType))
    status = gr.Field(gr.Enum.from_enum(constants.UserContextStatus))
    profile = gr.Field(lambda: Profile)
    created = gr.Field(gr.DateTime)
    updated = gr.Field(lambda: gr.DateTime)


class UserContextConnection(relay.Connection):
    class Meta:
        node = UserContext

    count = gr.Int()

    def resolve_count(self, info):
        return len(self.edges)


class ParticipantContext(SQLAlchemyObjectType):
    class Meta:
        model = models.ParticipantContext
        interfaces = (relay.Node, UserContext)
        exclude_fields = ("deleted",)


class FacilitatorContext(SQLAlchemyObjectType):
    class Meta:
        model = models.FacilitatorContext
        interfaces = (relay.Node, UserContext)
        exclude_fields = ("deleted",)


class Profile(SQLAlchemyObjectType):
    class Meta:
        model = models.Profile
        interfaces = (relay.Node,)


class Identity(SQLAlchemyObjectType):
    class Meta:
        model = models.Identity
        interfaces = (relay.Node,)


class NotificationPolicy(SQLAlchemyObjectType):
    class Meta:
        model = models.NotificationPolicy
        interfaces = (relay.Node,)


class FacilitatorLicense(SQLAlchemyObjectType):
    class Meta:
        model = models.FacilitatorLicense
        interfaces = (relay.Node,)
        exclude_fields = ("deleted",)


# class Company(SQLAlchemyObjectType):
#     class Meta:
#         model = models.Company
#         interfaces = (relay.Node,)


# class Employee(SQLAlchemyObjectType):
#     class Meta:
#         model = models.Employee
#         interfaces = (relay.Node,)

# class FinancialDetails(SQLAlchemyObjectType):
#     class Meta:
#         model = models.FinancialDetails
#         interfaces = (relay.Node,)
#         exclude_fields = ("subject", "provider")
