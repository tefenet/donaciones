import os
from config import config
from sqlalchemy import create_engine

from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

engine = create_engine(config.get(os.environ.get("FLASK_ENV")).SQLALCHEMY_URI)

dbSession = scoped_session(sessionmaker(bind=engine))
