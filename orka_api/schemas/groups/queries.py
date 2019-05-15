from graphql import GraphQLError
import graphene as gr
from graphene import relay


class Query(gr.ObjectType):
    pass
    # participant = gr.Field(Participant)
    # facilitator = gr.Field(Facilitator)
    # user = gr.Field(User, id=gr.Int(required=True))

    # def resolve_user(self, info, id):
    #     return User.get_query(info).filter(models.User.id == id).one()

    # def resolve_me(self, info):
    #     if info.context.current_jwt:
    #         if not info.context.current_user:
    #             raise GraphQLError("No account found")
    #         return info.context.current_user._get_current_object()

    #     else:
    #         raise GraphQLError("User Not authenticated")
