from app.models.sistema import Sistema
from app.db import Base
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, String, Boolean, DateTime, SmallInteger
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models.role import user_has_role


class User(Base):

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False, unique=True, index=True)
    username = Column(String, nullable=False, unique=True, index=True)
    password_hash = Column(String, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    active = Column(Boolean, index=True)
    create_date = Column(DateTime, default=datetime.now())
    update_date = Column(DateTime, default=None)
    user_roles = relationship(
        "Role",
        secondary=user_has_role,
        back_populates="role_users")

    def __init__(self, email=None, username=None, password=None, first_name=None, last_name=None, active=None):
        self.email = email
        self.username = username
        self.password_hash = password
        self.first_name = first_name
        self.last_name = last_name
        self.active = active

    def __repr__(self):
        return "<User(email='{}', id='{})'>".format(self.email, self.id)

    def set_password(self, password):
        """Genera un hash para la contraseña dada, y lo almacena en el campo password_hash del usuario"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Comprueba que la contraseña ingresada corresponda al hash almacenado"""
        return check_password_hash(self.password_hash, password)

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def updated(self):
        """Setea el campo update_date con datetime now"""
        self.update_date = datetime.now()

    def update(self, email, username, first_name, last_name):
        """Actualiza los datos del usuario"""
        self.email = email
        self.username = username
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def all(cls):
        """Retorna todos los usuarios de la clase User"""
        return cls.query.all()

    @classmethod
    def get_by_id(cls, user_id):
        """Retorna el usuario con id user_id"""
        return cls.query.get(user_id)

    @classmethod
    def find_by_username(cls, username):
        """Retorna una lista con los usuarios que contengan username en su nombre de usuario"""
        return list(cls.query.filter(cls.username.contains(username)))

    @classmethod
    def query_by_username(cls, username):
        return cls.query.filter(cls.username.contains(username))

    @classmethod
    def find_by_status(cls, status=True):
        """Recibe un nombre de usuario. Retorna una Query con los matches por username"""
        """Recibe un booleano indicando el estado(activo/inactivo).
         Retorna una lista con los usuarios que esten activos/inactivos"""
        return list(cls.query.filter(cls.active == status))

    @classmethod
    def query_by_status(cls, status):
        """Recibe un booleano indicando el estado(activo/inactivo). Retorna una Query"""

        return cls.query.filter(cls.active == status)

    @classmethod
    def delete_by_id(cls, id):
        """Elimina un usuario de la base de datos de forma permanente"""
        return cls.query.filter(cls.id == id).delete()

    def roles(self):
        """Retorna una lista con todos los roles del usuario"""
        return self.user_roles

    def has_role(self, r):  # podría pertenecer al controlador
        """Retorna True si el rol existe entre los roles del usuario"""
        return r in self.user_roles

    def add_role(self, role):
        """Agrega un rol a la relacion entre usuario y roles. También se agrega del lado del rol"""
        self.user_roles.append(role)

    def del_role(self, role):
        """
        Este metodo elimina un rol del usuario, tanto del lado del usuario como del lado del rol.
        Tiene que llegar si o si un role que este en el usuario, el chequeo debe estar en el controlador
        """
        self.user_roles.remove(role)

    def set_roles(self, roles):
        self.user_roles = roles


    def has_permission(self, perm):
        """Retorna el rol del user"""
        my_roles = list(self.user_roles)
        return any(role.has_permission(perm) for role in my_roles)
