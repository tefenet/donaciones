from flask import jsonify
from MySQLdb import TIMESTAMP, TIME
from sqlalchemy.dialects.mysql import ENUM
from sqlalchemy.orm import relationship
from sqlalchemy.orm.exc import NoResultFound

from app.db import Base, dbSession
from sqlalchemy import Column, Integer, String, Boolean, DateTime, LargeBinary, ForeignKey, Time, Enum
from datetime import datetime, date
import enum


from app.models.shifts import Shifts

STATES = ('pending', 'approved', 'rejected')
STATE_ENUM = ENUM(*STATES, name='state')
CENTER_TYPES = ('alimentos', 'general', 'salud')
CENTER_TYPES_ENUM = ENUM(*CENTER_TYPES, name='type')


class Center(Base):
    __tablename__ = 'centers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(40), nullable=False)
    address = Column(String(100), nullable=True)
    phone = Column(String(20))
    email = Column(String(60))
    web_site = Column(String(40))
    opening = Column(Time())
    closing = Column(Time())
    published = Column(Boolean(), default=False)
    state = Column(STATE_ENUM, default=STATES[0])
    gl_lat = Column(String(30))
    gl_long = Column(String(30))
    protocol = Column(LargeBinary())
    city_id = Column(Integer)
    center_type = Column(CENTER_TYPES_ENUM)
    shifts = relationship("Shifts", backref="center")

    def __init__(self, name=None, address=None, phone=None, email=None, opening=None, closing=None):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.opening = opening
        self.closing = closing
        self.published = False

    def __repr__(self):
        return "<Center(name='{}')'>".format(self.name, self.id)

    def __attrs__(self):
        return list(map(lambda s: s[0] + ' : ' + s[1].__str__(), self.__dict__.items()))[1:]

    def toogle_published(self):
        if self.published:
            self.published = False
        else:
            self.publish()
        dbSession.commit()

    def publish(self):
        if self.state == STATES[1]:
            self.published = True
        else:
            raise AttributeError('no se puede publicar si no está aprobado')

    def approve(self):
        self.state = STATES[1]
        self.published = True
        dbSession.commit()

    def reject(self):
        self.state = STATES[2]
        self.published = False
        dbSession.commit()

    def review(self):
        self.state = STATES[0]
        self.published = False
        dbSession.commit()

    def get_shifts_blocks_avalaible(self, date1=date.today()):
        """Retorna los bloques de horario disponibles para el día date1, para un centro dado"""
        shifts = self.get_shifts_by_date(date1)
        return Shifts.aval_shifts(self, shifts)

    def get_shifts_by_date(self, dt=date.today()):
        """Retorna los turnos asociados al día recibido. dt debe ser datetime.date
        Si no se recibe un día, retorna los turnos del día actual"""
        if not type(dt) is date:
            raise Exception("Error, la fecha debe ser un objeto datetime.date")
        # si no es un datetime.date va a devolver una lista vacía, y se va a poder agregar un turno que ya existe.
        return list(filter(lambda s: s.date == dt, self.shifts))

    def valid_start_time(self, start_time):
        """Chequeo que el horario del turno pertenezca a un horario válido"""
        return self.opening <= start_time < self.closing


    def serialized(self):
        """Serializa un centro de ayuda"""
        return {
            "nombre": self.name,
            "direccion": self.address,
            "telefono": self.phone,
            "hora_apertura": self.opening.isoformat(),
            "hora_cierre": self.closing.isoformat(),
            "tipo": self.center_type,
            "web": self.web_site,
            "email": self.email
        }


    def to_json(self):
        """Convierte un centro de ayuda a formato JSON"""
        return jsonify(self.serialized())


    @classmethod
    def delete_by_id(cls, id):
        """Elimina un centro de la base de datos de forma permanente"""
        return cls.query.filter(cls.id == id).delete()

    @classmethod
    def get_by_id(cls, centro_id):
        """Retorna el centro con id centro_id"""
        c = cls.query.get(centro_id)
        if c is None:
            raise NoResultFound('no existe un Centro con id {}'.format(centro_id))
        return c

    @classmethod
    def get_by_name(cls, center_name):
        """Retorna el centro con id centro_id"""
        return cls.query.filter(cls.name == center_name).first()

    @classmethod
    def query_by_name(cls, name):
        return cls.query.filter(cls.name.contains(name))

    @classmethod
    def query_by_state(cls, state):
        """Recibe un string indicando el estado. Retorna una Query"""
        return cls.query.filter(cls.state == state)

    @classmethod
    def get_for_index(cls):
        """Retorna una Query para el paginador, que tome los centro que no fueron rechazados"""
        return cls.query.filter(cls.state != STATES[2])

    @classmethod
    def query_by_published(cls, published):
        """Recibe un string indicando el estado. Retorna una Query"""
        return cls.query.filter(cls.published == published)

