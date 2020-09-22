from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from app.db import dbSession

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)

    def __repr__(self):
        return "<User(email='{}', id='{})'>".format(self.email, self.id)