from app.db import Base
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship

role_has_permission = Table('role_has_permission', Base.metadata,
                            Column('permissions_id', Integer, ForeignKey('permissions.id')),
                            Column('roles_id', Integer, ForeignKey('roles.id'))
                            )


class Permission(Base):
    __tablename__ = 'permissions'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    permission_roles = relationship(
        "Role",
        secondary=role_has_permission,
        back_populates="role_permissions")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Permission(name={}, id={})>".format(self.name, self.id)
