from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

from oshe.task.store import Store

Model = declarative_base()


class SqlalchemyStore(Store):
    db_uri = None
    db_table = None

    def __init__(self):
        if self.db_uri is None:
            raise Exception("Database URI has not been specified")
        if self.db_table is None:
            raise Exception("Database table has not been specified")

        engine = create_engine(self.db_uri)
        session = scoped_session(sessionmaker(bind=engine))
        self.engine = engine
        self.session = session
        self.Model = Model

        self.create_all()

    def create_all(self):
        self.Model.metadata.create_all(self.engine)

    def drop_all(self):
        self.Model.metadata.drop_all(self.engine)

    def store(self, **kwargs):
        raise NotImplementedError
