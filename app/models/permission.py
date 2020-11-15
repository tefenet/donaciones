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

    def roles(self):
        """Retorna una lista con todos los roles del permiso"""
        return self.permission_roles

    def has_role(self, r):  # podría pertenecer al controlador
        """Retorna True si el rol existe entre los roles del permiso"""
        return r in self.permission_roles

    def add_role(self, role):
        """Agrega un rol a la relacion entre permiso y roles. También se agrega del lado del rol"""
        self.permission_roles.append(role)

    def del_role(self, role):
        """
        Este metodo elimina un rol del permiso, tanto del lado del usuario como del lado del rol.
        Tiene que llegar si o si un role que este en el permiso, el chequeo debe estar en el controlador
        """
        self.permission_roles.remove(role)

    @classmethod
    def get_by_name(cls, permission_name):
        """Retorna el usuario con id user_id"""
        return cls.query.filter(cls.name.contains(permission_name)).first()
