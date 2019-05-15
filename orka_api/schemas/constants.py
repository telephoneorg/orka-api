import graphene as gr

from .. import constants


UserContextType = gr.Enum.from_enum(constants.UserContextType)
UserContextStatus = gr.Enum.from_enum(constants.UserContextStatus)
IdentityProvider = gr.Enum.from_enum(constants.IdentityProvider)
PaymentProcessor = gr.Enum.from_enum(constants.PaymentProcessor)
LicenseType = gr.Enum.from_enum(constants.LicenseType)
UsState = gr.Enum.from_enum(constants.UsState)
