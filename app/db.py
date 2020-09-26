from os import environ
from config import config
from sqlalchemy import create_engine

from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

engine = create_engine(config.get(environ.get("FLASK_ENV")).SQLALCHEMY_URL)

dbSession = scoped_session(sessionmaker(bind=engine))
