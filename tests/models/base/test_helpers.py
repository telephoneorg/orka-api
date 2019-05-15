import pytest

from orka_api.models.base.helpers import (
    recursive_create,
    recursive_patch,
    recursive_soft_delete,
)

NEW_USER_PAYLOAD = dict(
    user=dict(
        first_name="Joe",
        last_name="White",
        email="joe@example.com",
        cell_phone="6469247718",
        notification_policy=dict(
            allow_sms=True, allow_email=True, allow_marketing=True
        ),
    )
)

PATCH_USER_PAYLOAD = dict(
    user=dict(
        last_name="White",
        cell_phone="6666666666",
        notification_policy=dict(allow_marketing=False),
    )
)


def recursive_verify(model, payload):
    for key, val in payload.items():
        if isinstance(val, dict):
            recursive_verify(getattr(model, key), val)
        else:
            assert payload.get(key) == val


@pytest.fixture
def new_user(db):
    payload = NEW_USER_PAYLOAD.get("user")
    new_user = recursive_create("User", **payload)
    db.session.add(new_user)
    db.session.commit()
    yield new_user

    db.reset_db()


def test_recursive_create_model(new_user):
    payload = NEW_USER_PAYLOAD.get("user")
    recursive_verify(new_user, payload)


def test_recursive_patch_model(new_user):
    patch_payload = PATCH_USER_PAYLOAD.get("user")
    recursive_patch(new_user, patch_payload)
    recursive_verify(new_user, patch_payload)


def test_recursive_soft_delete(new_user):
    user = recursive_soft_delete(new_user)
    assert new_user.deleted is True
