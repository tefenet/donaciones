from app.db import Base
from sqlalchemy import Column, Integer, String


class Permission(Base):
    __tablename__ = 'permissions'
    id = Column(Integer, primary_key=True)
    name = Column(String)


    def __init__(self, name):
        self.name = name
