from flask_admin.contrib.sqla import ModelView

from .. import models

# Flask and Flask-SQLAlchemy initialization here

from datetime import date, datetime
from flask_admin.model import typefmt


def date_format(view, value):
    return value.strftime("%m/%d/%Y")


def datetime_format(view, value):
    return value.strftime("%m/%d/%Y %H:%M:%S")


MY_DEFAULT_FORMATTERS = dict(typefmt.BASE_FORMATTERS)
MY_DEFAULT_FORMATTERS.update(
    {
        type(None): typefmt.null_formatter,
        datetime: datetime_format,
        date: date_format,
    }
)


class OrkaApiModelView(ModelView):
    column_type_formatters = MY_DEFAULT_FORMATTERS
    can_set_page_size = True
    page_size = 50  # the number of entries to display on the list view
    can_view_details = True
    create_modal = True
    edit_modal = True
    can_export = True


class UsersModelView(OrkaApiModelView):
    _model = models.User
    _category = "Users"
    inline_models = [models.ParticipantContext, models.FacilitatorContext]
    # column_exclude_list = []
    column_list = [
        "first_name",
        "last_name",
        "email",
        "cell_phone",
        "dob",
        "deleted",
        "created",
        "updated",
    ]
    # column_details_list = ["notification_policy", "contexts"]
    column_searchable_list = [
        "first_name",
        "last_name",
        "email",
        "cell_phone",
        "dob",
    ]
    column_filters = ["deleted"]
    column_editable_list = ["first_name", "last_name", "cell_phone", "dob"]
    form_excluded_columns = ["deleted", "created", "updated"]
    # inline_models = ["contexts", "identities"]


class ParticipantContextModelView(OrkaApiModelView):
    _model = models.ParticipantContext
    _category = "Users"
    # inline_models = [models.User]
    column_list = ["user", "status", "deleted", "created", "updated"]
    column_select_related_list = ["user"]
    column_exclude_list = ["type"]
    # column_searchable_list = []
    column_filters = ["deleted", "type", "status"]
    column_editable_list = ["status"]
    form_excluded_columns = ["deleted", "type", "created", "updated"]
    # inline_models = ["profile"]


class FacilitatorContextModelView(ParticipantContextModelView):
    _model = models.FacilitatorContext
    _category = "Users"
    inline_models = [models.FacilitatorLicense]
    column_list = ["user", "npi", "status", "deleted", "created", "updated"]
    column_searchable_list = ["npi"]
    form_excluded_columns = ["deleted", "type", "created", "updated"]


class NotificationPolicyModelView(OrkaApiModelView):
    _model = models.NotificationPolicy
    _category = "Users"
    # column_exclude_list = ["type"]
    # column_searchable_list = []
    column_list = [
        "user",
        "allow_email",
        "allow_sms",
        "allow_marketing",
        "created",
        "updated",
    ]
    column_select_related_list = ["user"]
    column_filters = ["allow_email", "allow_sms", "allow_marketing"]
    column_editable_list = ["allow_email", "allow_sms", "allow_marketing"]
    form_excluded_columns = ["created", "updated"]
    # inline_models = ["profile"]


class ProfileModelView(OrkaApiModelView):
    _model = models.Profile
    _category = "Users"
    # column_exclude_list = ["type"]
    column_list = [
        "user_context",
        "display_name",
        "avatar",
        "created",
        "updated",
    ]
    column_select_related_list = ["user_context"]
    column_searchable_list = ["display_name", "avatar", "bio"]
    # column_filters = ["allow_email", "allow_sms", "allow_marketing"]
    column_editable_list = ["display_name", "avatar"]
    form_excluded_columns = ["created", "updated"]


class FacilitatorLicenseModelView(OrkaApiModelView):
    _model = models.FacilitatorLicense
    _category = "Users"
    # column_exclude_list = ["type"]
    column_list = [
        "facilitator_context",
        "type",
        "number",
        "expiry",
        "us_state",
        "deleted",
        "created",
        "updated",
    ]
    column_select_related_list = ["facilitator_context"]
    column_searchable_list = ["number"]
    column_filters = ["deleted", "type", "expiry", "us_state"]
    column_editable_list = ["type", "number", "expiry", "us_state"]
    form_excluded_columns = ["created", "updated"]
    # inline_models = ["profile"]


def register_views(admin, db):
    for view in [
        UsersModelView,
        ParticipantContextModelView,
        FacilitatorContextModelView,
        NotificationPolicyModelView,
        ProfileModelView,
        FacilitatorLicenseModelView,
    ]:
        admin.add_view(view(view._model, db.session, category=view._category))
