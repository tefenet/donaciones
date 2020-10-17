from app.db import Base
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, String, Boolean, DateTime, SmallInteger
from datetime import datetime


class User(Base):
    """
    account type = 1 --> administrator
    account type != 1 --> user
    """

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False, unique=True, index=True)
    username = Column(String, nullable=False, unique=True, index=True)
    password_hash = Column(String, nullable=False)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    active = Column(Boolean, index=True)
    account_type = Column(SmallInteger, default=2)
    create_date = Column(DateTime, default=datetime.now())
    update_date = Column(DateTime, default=None)

    def __init__(self, email=None, username=None, password=None, first_name=None, last_name=None, account_type=2,
                 active=None):
        self.email = email
        self.username = username
        self.password_hash = password
        self.first_name = first_name
        self.last_name = last_name
        self.account_type = account_type
        self.active = active

    def __repr__(self):
        return "<User(email='{}', id='{})'>".format(self.email, self.id)

    def set_password(self, password):
        """Genera un hash para la contraseña dada, y lo almacena en el campo password_hash del usuario"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Comprueba que la contraseña ingresada corresponda al hash almacenado"""
        return check_password_hash(self.password_hash, password)

    def updated(self):
        """Setea el campo update_date con datetime now"""
        self.update_date = datetime.now()

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
        return list(cls.query.filter(User.username.contains(username)))

    @classmethod
    def find_by_status(cls, status=True):
        """Recibe un booleano indicando el estado(activo/inactivo).
         Retorna una lista con los usuarios que esten activos/inactivos"""
        return list(cls.query.filter(User.active == status))
