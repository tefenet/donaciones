from app.db import Base
from sqlalchemy import Column, Integer, String, Boolean
from datetime import datetime


class Sistema(Base):
    """
    Modelo de configuración del sistema
    
    """

    __tablename__ = 'sistema'
    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    descripcion = Column(String, nullable=False)
    bienvenida = Column(String)
    email = Column(String(25), nullable=False)
    cant_por_pagina = Column(Integer, nullable=False)
    habilitado = Column(Boolean, default=True)
    


    def __init__(self, titulo=None, descripcion=None, bienvenida=None, email=None, cant_por_pagina=None):
        self.titulo = titulo
        self.descripcion = descripcion
        self.bienvenida = bienvenida   
        self.email = email
        self.cant_por_pagina = cant_por_pagina 
        

    def __repr__(self):
        return "<Sistema(titulo='{}')'>".format(self.titulo, self.id)
