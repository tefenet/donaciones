from app.db import Base
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, String, Boolean, DateTime, SmallInteger
from datetime import datetime


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    username = Column(String)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    active = Column(Boolean)
    account_type = Column(SmallInteger)
    create_date = Column(DateTime, default=datetime.now())

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
