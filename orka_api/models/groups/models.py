from sqlalchemy import (
    Column,
    Enum,
    ForeignKey,
    Integer,
    Table,
    Boolean,
    Unicode,
    UnicodeText,
    DateTime,
)
from sqlalchemy.orm import relationship, validates, backref
from sqlalchemy_utils import generic_repr


from ... import constants
from ..base import Base, TimestampMixin, utcnow


@generic_repr
class Recurrence(Base):
    __tablename__ = "recurrences"

    id = Column(Integer, primary_key=True)
    start_datetime = Column(DateTime)
    end_datetime = Column(DateTime)
    freq = Column(
        Enum(constants.TimePeriod), default=constants.TimePeriod.WEEK
    )
    interval = Column(Integer, nullable=False, default=1)


@generic_repr
class Community(Base, TimestampMixin):
    __tablename__ = "communities"

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), nullable=False)
    slug = Column(Unicode(255), nullable=False)
    description = Column(UnicodeText)
    photo = Column(Unicode(255))
    cover_photo = Column(Unicode(255))
    status = Column(
        Enum(constants.BasicStatus), default=constants.BasicStatus.ACTIVE
    )

    groups = relationship("Group", secondary="community_groups")
    members = relationship("CommunityMember", back_populates="community")


@generic_repr
class Group(Base, TimestampMixin):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True)
    facilitator_id = Column(
        ForeignKey("user_contexts.id"), nullable=False, index=True
    )
    name = Column(Unicode(255), nullable=False)
    slug = Column(Unicode(255), nullable=False)
    description = Column(UnicodeText)
    photo = Column(Unicode(255))
    cover_photo = Column(Unicode(255))
    recurrence_id = Column(ForeignKey("recurrences.id"), nullable=False)

    credit_cost = Column(Integer, default=1)

    recurrence = relationship(
        "Recurrence", uselist=False, backref=backref("group", uselist=False)
    )
    # facilitator = relationship("Facilitator", backref="groups")
    participants = relationship("GroupMember", back_populates="group")


community_groups = Table(
    "community_groups",
    Base.metadata,
    Column(
        "community_id",
        ForeignKey("communities.id"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "group_id",
        ForeignKey("groups.id"),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


@generic_repr
class CommunityMember(Base):
    __tablename__ = "community_members"

    community_id = Column(
        ForeignKey("communities.id"), primary_key=True, nullable=False
    )
    user_context_id = Column(
        ForeignKey("user_contexts.id"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    joined = Column(DateTime, nullable=False, default=utcnow)
    left = Column(DateTime)

    community = relationship("Community", back_populates="members")
    user_context = relationship("UserContext", back_populates="communities")


@generic_repr
class GroupMember(Base):
    __tablename__ = "group_members"

    group_id = Column(
        ForeignKey("groups.id"), primary_key=True, nullable=False
    )
    participant_id = Column(
        ForeignKey("user_contexts.id"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    joined = Column(DateTime, nullable=False, default=utcnow)
    left = Column(DateTime)

    group = relationship("Group", back_populates="participants")
    participant = relationship("ParticipantContext", back_populates="groups")

    @validates("participant")
    def validate_participant(self, key, obj):
        obj.__class__.__name__ == "Participant"
        return obj


@generic_repr
class GroupSession(Base):
    __tablename__ = "group_sessions"

    id = Column(Integer, primary_key=True)
    group_id = Column(ForeignKey("groups.id"), nullable=False, index=True)
    facilitator_id = Column(
        ForeignKey("user_contexts.id"), nullable=False, index=True
    )
    topic = Column(Unicode(255))
    description = Column(UnicodeText)

    facilitator = relationship("FacilitatorContext")
    group = relationship("Group")
    participants = relationship(
        "ParticipantContext", secondary="attended_group_sessions"
    )


t_attended_group_sessions = Table(
    "attended_group_sessions",
    Base.metadata,
    Column(
        "group_session_id",
        ForeignKey("group_sessions.id"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "participant_id",
        ForeignKey("user_contexts.id"),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)
