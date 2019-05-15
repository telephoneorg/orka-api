from datetime import datetime, date, timedelta, timezone

import pytest

from orka_api.database import DataAccessLayer

from orka_api import models


class MockCognitoUser:
    def __init__(self, user=None, jwt=None):
        self.user = user
        self.jwt = jwt

    @property
    def is_anonymous(self):
        return not self.is_authenticated

    @property
    def is_authenticated(self):
        return bool(self.jwt and self.jwt.get("sub"))

    @property
    def is_in_database(self):
        return bool(self.user)

    @property
    def email(self):
        return self.jwt.get("email")

    @property
    def subject(self):
        return self.jwt.get("sub")


@pytest.fixture
def db():
    database = DataAccessLayer("sqlite:///:memory:").connect().init_db()
    yield database
    database.reset_db()


@pytest.fixture
def current_user(db):
    def current_user_factory(user=None, jwt=None):
        if user is None:
            user = models.User(
                first_name="John",
                last_name="Smith",
                email="johnsmith@gmail.com",
                dob=date(1980, 1, 4),
                cell_phone="+14153334444",
                contexts=[
                    models.ParticipantContext(
                        profile=models.Profile(
                            display_name="Johnny",
                            avatar="https://example.com/images/me.jpg",
                            bio="Hey!\n\nWhat are you looking at?",
                        )
                    ),
                    models.FacilitatorContext(
                        npi="nc2394jt98ddeesd",
                        availability='[{"isoWeekDay": 1, "start": "14:49:31.947740", "end": "22:49:31.947749"}, {"isoWeekDay": 2, "start": "14:49:31.947758", "end": "22:49:31.947760"}, {"isoWeekDay": 3, "start": "14:49:31.947765", "end": "22:49:31.947766"}, {"isoWeekDay": 4, "start": "14:49:31.947770", "end": "22:49:31.947772"}, {"isoWeekDay": 5, "start": "14:49:31.947776", "end": "22:49:31.947777"}, {"isoWeekDay": 6, "start": "14:49:31.947781", "end": "22:49:31.947782"}, {"isoWeekDay": 7, "start": "14:49:31.947786", "end": "22:49:31.947788"}]',
                        profile=models.Profile(
                            display_name="Dr. Smith",
                            avatar="https://dr-smith.com/photos/dr-smith.jpg",
                            bio="I don't know how to put this but I'm kind of a big deal.\n\n People know me. I'm very important. \n\nI have many leather-bound books and my apartment smells of rich mahogany.",
                        ),
                        licenses=[
                            models.FacilitatorLicense(
                                number="xpii23420e90",
                                type="TBD",
                                expiry=date(2022, 2, 8),
                                us_state="NY",
                            ),
                            models.FacilitatorLicense(
                                number="xpn342300309e8", type="TBD"
                            ),
                            models.FacilitatorLicense(
                                number="expired",
                                type="TBD",
                                expiry=date(2016, 2, 8),
                                us_state="NY",
                            ),
                        ],
                    ),
                ],
                notification_policy=models.NotificationPolicy(
                    allow_marketing=False, allow_email=True, allow_sms=True
                ),
                identities=[
                    models.Identity(
                        provider="CUP",
                        subject="25f7ac7d-d997-44b5-b8a9-7da2a14b1013",
                    )
                ],
            )
            db.session.add(user)
            db.session.commit()
        elif user is False:
            user = None

        if jwt is None:
            jwt = dict(
                email="johnsmith@gmail.com",
                sub="25f7ac7d-d997-44b5-b8a9-7da2a14b1013",
            )
        elif jwt is False:
            jwt = None

        return MockCognitoUser(user, jwt)

    return current_user_factory
