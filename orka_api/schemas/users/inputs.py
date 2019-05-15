import graphene as gr
from .. import constants


class ProfileFields(gr.AbstractType):
    display_name = gr.String()
    avatar = gr.String()
    bio = gr.String()


class ProfileInput(gr.InputObjectType, ProfileFields):
    display_name = gr.String()
    avatar = gr.String()
    bio = gr.String()


class NotificationPolicyFields(gr.AbstractType):
    allow_email = gr.Boolean()
    allow_sms = gr.Boolean()
    allow_marketing = gr.Boolean()


class NotificationPolicyInput(gr.InputObjectType, NotificationPolicyFields):
    pass


class UserFields(gr.AbstractType):
    first_name = gr.String()
    last_name = gr.String()
    cell_phone = gr.String()
    dob = gr.Date()
    notification_policy = gr.Field(lambda: NotificationPolicyInput)


class UserInput(gr.InputObjectType, UserFields):
    pass


class NewUserFields(UserFields):
    first_name = gr.String(required=True)
    last_name = gr.String(required=True)
    dob = gr.Date(required=True)
    notification_policy = gr.Field(
        lambda: NotificationPolicyInput, required=True
    )


class ParticipantContextFields(gr.AbstractType):
    profile = gr.Field(ProfileInput)


class ParticipantContextInput(gr.InputObjectType, ParticipantContextFields):
    pass


class NewParticipantContextFields(ParticipantContextFields):
    profile = gr.Field(ProfileInput, required=True)


class UpdateParticipantContextFields(gr.AbstractType):
    id = gr.GlobalID(required=True)
    participant_context = gr.Field(lambda: ParticipantContextInput)


class FacilitatorContextFields(ParticipantContextFields):
    npi = gr.String()
    availability = gr.String()
    licenses = gr.List(lambda: FacilitatorLicenseInput)


class FacilitatorContextInput(gr.InputObjectType, FacilitatorContextFields):
    pass


class NewFacilitatorContextFields(FacilitatorContextFields):
    npi = gr.String(required=True)
    availability = gr.String(required=True)


class UpdateFacilitatorContextFields(gr.AbstractType):
    id = gr.GlobalID(required=True)
    facilitator_context = gr.Field(lambda: FacilitatorContextInput)


class FacilitatorLicenseInput(gr.InputObjectType):
    type = constants.LicenseType()
    number = gr.String()
    expiry = gr.Date()
    us_state = constants.UsState()
