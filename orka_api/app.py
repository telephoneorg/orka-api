from munch import Munch

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_graphql import GraphQLView
from flask_cors import CORS

from .cognito_auth import CognitoAuth, cognito_user, load_cognito_tokens
from .schemas import schema
from . import models


app = Flask(__name__)
app.config.from_object("orka_api.config.Config")
db = SQLAlchemy(app, metadata=models.Base.metadata)
cogauth = CognitoAuth(app)
cors = CORS(
    app,
    supports_credentials=app.config["CORS_ALLOW_CREDENTIALS_GLOBAL"],
    origins=app.config["CORS_ORIGINS_GLOBAL"],
    max_age=app.config["CORS_MAX_AGE"],
)


app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view(
        "graphql",
        schema=schema,
        graphiql=True,
        get_context=lambda request=None: Munch(
            request=request, session=db.session, current_user=cognito_user
        ),
    ),
)

app.before_request(load_cognito_tokens)


@cogauth.identity_handler
def lookup_cognito_user(payload):
    user = (
        db.session.query(models.User)
        .join(models.Identity, models.User.id == models.Identity.user_id)
        .filter(models.Identity.subject == payload["sub"])
        .one_or_none()
    )
    return user


# @app.before_first_request
# def setup():
#     models.Base.query = db.session.query_property()
