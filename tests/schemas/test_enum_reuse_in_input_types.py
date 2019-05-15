import graphene as gr
from graphene.types.typemap import TypeMap


from orka_api import constants


LicenseType = gr.Enum.from_enum(constants.LicenseType)


def test_input_enum_type_reuse_works():
    class LicenseInputType(gr.InputObjectType):
        type = LicenseType()

    class License(gr.ObjectType):
        type = LicenseType()

    typemap = TypeMap([License, LicenseInputType])
    return typemap
