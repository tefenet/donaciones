from app.db import Base
from sqlalchemy import Column, Integer, String


class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(String)


    def __init__(self, name):
        self.name = name
