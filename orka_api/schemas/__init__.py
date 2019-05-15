import graphene as gr

from .users import Query as UsersQuery, Mutation as UsersMutation
from .groups import Query as GroupsQuery, Mutation as GroupsMutation


class Query(UsersQuery, GroupsQuery, gr.ObjectType):
    pass


class Mutation(UsersMutation, GroupsMutation, gr.ObjectType):
    pass


schema = gr.Schema(query=Query, mutation=Mutation)
