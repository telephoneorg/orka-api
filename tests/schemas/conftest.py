import munch
import pytest
from graphene.test import Client

from orka_api.schemas import schema


@pytest.fixture
def graphene_client():
    return Client(schema)


@pytest.fixture
def graphene_context(db, current_user):
    def graphene_context_factory(
        request=None, session=None, user=None, jwt=None
    ):
        session = session or db.session
        user = current_user(user=user, jwt=jwt)
        return munch.Munch(request=request, session=session, current_user=user)

    return graphene_context_factory
