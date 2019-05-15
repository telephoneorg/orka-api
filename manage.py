import os
import sys

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

from orka_api.config import Config
from orka_api import models

LOCAL = False


def _get_db_engine():
    return create_engine(Config.SQLALCHEMY_DATABASE_URI)


def _get_metadata():
    return models.Base.metadata


def init_db():
    if LOCAL:
        os.chdir("orka_api")
    engine = _get_db_engine()
    metadata = _get_metadata()
    if not database_exists(engine.url):
        create_database(engine.url)

    return metadata.create_all(bind=engine)


def clear_db():
    if LOCAL:
        os.chdir("orka_api")
    engine = _get_db_engine()
    metadata = _get_metadata()
    return (metadata.drop_all(bind=engine), metadata.create_all(bind=engine))


def show_users():
    from orka_api.app import db

    users = db.session.query(models.User).all()
    return "\n".join([repr(user) for user in users])


def show_identities():
    from orka_api.app import db

    ids = db.session.query(models.Identity).all()
    return "\n".join([repr(id) for id in ids])


if __name__ == "__main__":
    LOCAL = True
    func_name = sys.argv[1]
    print(f"SQLALCHEMY_DATABASE_URI: {Config.SQLALCHEMY_DATABASE_URI}")
    print(globals().get(func_name)())
