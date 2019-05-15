from sqlalchemy import (
    Column,
    Enum,
    ForeignKey,
    Integer,
    Boolean,
    Unicode,
    UnicodeText,
    Date,
)
from sqlalchemy.orm import relationship, validates
from sqlalchemy_utils import generic_repr


from ... import constants
from ..base import Base, TimestampMixin, SoftDeletable


@generic_repr
class User(Base, TimestampMixin, SoftDeletable):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(Unicode(255), nullable=False)
    last_name = Column(Unicode(255), nullable=False)
    email = Column(Unicode(255), nullable=False, unique=True)
    cell_phone = Column(Unicode(255))
    dob = Column(Date)

    identities = relationship("Identity", back_populates="user")
    contexts = relationship("UserContext", back_populates="user")
    notification_policy = relationship(
        "NotificationPolicy", back_populates="user", uselist=False
    )
    financial_details = relationship(
        "FinancialDetails", back_populates="user", uselist=False
    )


@generic_repr
class UserContext(Base, TimestampMixin, SoftDeletable):
    __tablename__ = "user_contexts"
    __mapper_args__ = {"polymorphic_on": "type"}

    id = Column(Integer, primary_key=True)
    type = Column(Enum(constants.UserContextType))
    user_id = Column(ForeignKey("users.id"), nullable=False, index=True)
    status = Column(
        Enum(constants.UserContextStatus),
        nullable=False,
        default=constants.UserContextStatus.CREATED,
    )

    user = relationship("User", back_populates="contexts")
    profile = relationship(
        "Profile", uselist=False, back_populates="user_context"
    )
    communities = relationship("CommunityMember")
    groups = relationship("GroupMember")


@generic_repr
class ParticipantContext(UserContext):
    __mapper_args__ = {
        "polymorphic_identity": constants.UserContextType.PARTICIPANT,
        "polymorphic_load": "inline",
    }


@generic_repr
class FacilitatorContext(UserContext):
    __mapper_args__ = {
        "polymorphic_identity": constants.UserContextType.FACILITATOR,
        "polymorphic_load": "inline",
    }

    npi = Column(Unicode(255))
    availability = Column(UnicodeText)

    licenses = relationship(
        "FacilitatorLicense", back_populates="facilitator_context"
    )


@generic_repr
class Profile(Base, TimestampMixin):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True)
    user_context_id = Column(
        ForeignKey("user_contexts.id"), nullable=False, index=True
    )
    display_name = Column(Unicode(255))
    avatar = Column(Unicode(255))
    bio = Column(UnicodeText)

    user_context = relationship(
        "UserContext", uselist=False, back_populates="profile"
    )


@generic_repr
class Identity(Base, TimestampMixin):
    __tablename__ = "identities"

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("users.id"), nullable=False, index=True)
    provider = Column(
        Enum(constants.IdentityProvider),
        nullable=False,
        default=constants.IdentityProvider.CUP,
    )
    subject = Column(Unicode(255), nullable=False)

    user = relationship("User", back_populates="identities")


@generic_repr
class NotificationPolicy(Base, TimestampMixin):
    __tablename__ = "notification_policies"

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("users.id"), nullable=False, index=True)
    allow_email = Column(Boolean, default=True)
    allow_sms = Column(Boolean, default=True)
    allow_marketing = Column(Boolean, default=True)

    user = relationship(
        "User", back_populates="notification_policy", uselist=False
    )


@generic_repr
class FinancialDetails(Base, TimestampMixin):
    __tablename__ = "financial_details"

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("users.id"), nullable=False, index=True)
    processor = Column(Enum(constants.PaymentProcessor))
    subject = Column(Unicode(255))

    user = relationship("User", back_populates="financial_details")


@generic_repr
class FacilitatorLicense(Base, TimestampMixin, SoftDeletable):
    __tablename__ = "facilitator_licenses"

    id = Column(Integer, primary_key=True)
    facilitator_context_id = Column(
        ForeignKey("user_contexts.id"), nullable=False, index=True
    )
    type = Column(
        Enum(constants.LicenseType),
        nullable=False,
        default=constants.LicenseType.TBD,
    )
    number = Column(Unicode(255), nullable=False)
    expiry = Column(Date)
    us_state = Column(Enum(constants.UsState))

    facilitator_context = relationship(
        "FacilitatorContext", back_populates="licenses"
    )

    @validates("facilitator_context")
    def validate_facilitator(self, key, obj):
        assert isinstance(obj, FacilitatorContext)
        return obj


# @generic_repr
# class Employee(Participant):
#     __mapper_args__ = {
#         "polymorphic_identity": constants.UserContextType.EMPLOYEE
#     }

#     company_id = Column(ForeignKey("user_contexts.id"), index=True)
#     company = relationship(
#         "Company",
#         uselist=False,
#         remote_side="Employee.id",
#         back_populates="employees",
#     )

#     @validates("company")
#     def validate_company(self, key, obj):
#         assert isinstance(obj, Company)
#         return obj


# @generic_repr
# class Company(UserContext):
#     __mapper_args__ = {
#         "polymorphic_identity": constants.UserContextType.COMPANY
#     }

#     employees = relationship("Employee", back_populates="company")

#     @validates("employees")
#     def validate_employees(self, key, obj):
#         assert isinstance(obj, Employee)
#         return obj
