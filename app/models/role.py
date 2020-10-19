from app.db import Base
from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

user_has_role = Table('user_has_role', Base.metadata,
                      Column('roles_id', Integer, ForeignKey('roles.id')),
                      Column('users_id', Integer, ForeignKey('users.id'))
                      )


class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    role_users = relationship(
        "User",
        secondary=user_has_role,
        back_populates="user_roles")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Role(name={}, id={})>".format(self.name, self.id)
