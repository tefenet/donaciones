from app.db import Base
from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from app.models.permission import role_has_permission

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
    role_permissions = relationship(
        "Permission",
        secondary=role_has_permission,
        back_populates="permission_roles")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Role(name={}, id={})>".format(self.name, self.id)

    def users(self):
        return self.role_users

    def permissions(self):
        return self.role_permissions

    def has_user(self, u):
        return u in self.role_users

    def has_permission(self, perm):
        return perm in self.role_permissions

    def add_user(self, user):
        """Agrega un usuario a la relacion entre rol y usuario. También se agrega del lado del usuario"""
        self.role_users.append(user)

    def del_user(self, user):
        """
        Este metodo elimina un usaurio de la relacion de rol y usuario, tanto del lado del rol como del lado del usuario.
        Tiene que llegar si o si un usuario que este en el rol, el chequeo debe estar en el controlador
        """
        self.role_users.remove(user)

    def add_permission(self, perm):
        """Agrega un permiso a la relacion entre rol y permiso. También se agrega del lado del permiso"""
        self.role_permissions.append(perm)

    def del_permission(self, perm):
        """
        Este metodo elimina un permiso de la relacion de rol y permiso, tanto del lado del rol como del lado del permiso.
        Tiene que llegar si o si un permiso que este en el rol, el chequeo debe estar en el controlador
        """
        self.role_permissions.remove(perm)

    @classmethod
    def get_role_by_name(cls, name):
        return cls.query.filter(cls.name == name).first()
