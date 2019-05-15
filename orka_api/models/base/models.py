import sqlalchemy as sa
from sqlalchemy import event, inspect
from sqlalchemy.orm.query import Query
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import observes
from slugify import slugify

from .utils import utcnow


Base = declarative_base()


class TimestampMixin:
    created = sa.Column(sa.DateTime, nullable=False, default=utcnow)
    updated = sa.Column(
        sa.DateTime, nullable=False, default=utcnow, onupdate=utcnow
    )


class HasSlug:
    slug = sa.Column(sa.Unicode(255), nullable=False)

    @observes("name")
    def _generate_slug(self, name):
        self.slug = slugify(name)


@event.listens_for(Query, "before_compile", retval=True)
def before_compile(query):
    """A query compilation rule that will add limiting criteria for every
    subclass of HasPrivate"""

    if query._execution_options.get("include_deleted", False):
        return query

    for ent in query.column_descriptions:
        entity = ent["entity"]
        if entity is None:
            continue
        insp = inspect(ent["entity"])
        mapper = getattr(insp, "mapper", None)
        if mapper and issubclass(mapper.class_, SoftDeletable):
            query = query.enable_assertions(False).filter(
                ent["entity"].deleted == False
            )

    return query


class SoftDeletable(object):
    """Mixin that identifies a class as having private entities"""

    deleted = sa.Column(sa.Boolean, nullable=False, default=False)


# the recipe has a few holes in it, unfortunately, including that as given,
# it doesn't impact the JOIN added by joined eager loading.   As a guard
# against this and other potential scenarios, we can check every object as
# its loaded and refuse to continue if there's a problem
@event.listens_for(SoftDeletable, "load", propagate=True)
def load(obj, context):
    if obj.deleted and not context.query._execution_options.get(
        "include_deleted", False
    ):
        raise TypeError(
            "deleted object %s was loaded, did you use "
            "joined eager loading?" % obj
        )
