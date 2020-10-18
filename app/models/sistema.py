from app.db import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime


class Sistema(Base):
    """
    Modelo de configuración del sistema

    users_table = op.create_table(
        'sistema',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('titulo', sa.String(100), index=True),
        sa.Column('descripcion', sa.String(), nullable=True),
        sa.Column('bienvenida', sa.String(), nullable=True),
        sa.Column('email', sa.String(100), index=True),
        sa.Column('cant_por_pagina', sa.SmallInteger(), nullable=False),
        sa.Column('habilitado', sa.Boolean(), default=False),
        sa.Column('update_date', sa.DateTime, nullable=True)
    """

    __tablename__ = 'sistema'
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(50))
    descripcion = Column(String())
    bienvenida = Column(String())
    email = Column(String(25))
    cant_por_pagina = Column(Integer, nullable=False, default=20)
    update_date = Column(DateTime())
    habilitado = Column(Boolean(), default=False)

    def __init__(self, titulo=None, descripcion=None, bienvenida=None, email=None, cant_por_pagina=None):
        self.titulo = titulo
        self.descripcion = descripcion
        self.bienvenida = bienvenida
        self.email = email
        self.cant_por_pagina = cant_por_pagina

    def __update__(self):
        self.update_date = datetime.now()

    def register_update(self):
        self.__update__()

    def __repr__(self):
        return "<Sistema(titulo='{}')'>".format(self.titulo, self.id)

    @classmethod
    def get_sistema(cls):
        return cls.query.first()
