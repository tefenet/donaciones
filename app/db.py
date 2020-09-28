from os import environ

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from config import config

engine = create_engine(config.get(environ.get("FLASK_ENV")).SQLALCHEMY_URI)

dbSession = scoped_session(sessionmaker(autocommit=False,
                                        autoflush=False, bind=engine))

Base = declarative_base()
Base.query = dbSession.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import app.models
    Base.metadata.create_all(bind=engine)
