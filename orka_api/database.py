from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DataAccessLayer:
    def __init__(self, conn_string="sqlite:///db.db"):
        self.engine = None
        self.conn_string = conn_string

    def connect(self):
        self.engine = create_engine(self.conn_string)
        self.session = scoped_session(
            sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        )
        return self

    def init_db(self):
        self.reset_db()
        return self

    def reset_db(self):
        from .models import Base

        Base.metadata.drop_all(self.engine)
        Base.metadata.create_all(self.engine)


dal = DataAccessLayer()
