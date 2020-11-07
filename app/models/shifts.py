from app.db import Base
from sqlalchemy import Column, Integer, ForeignKey, String, Time, Date

from app.models.center import Center
from datetime import datetime, date, timedelta, time

shift_time_blocks = [time(9), time(9, 30), time(10), time(10, 30), time(11), time(11, 30), time(12), time(12, 30),
                     time(13), time(13, 30), time(14), time(14, 30), time(15), time(15, 30)]


def shift_time_block(center):
    shifts = [center.opening]

    def fo(t):
        return (datetime.datetime(1, 1, 1, t.hour, t.minute) + timedelta(minutes=30)).time()

    while shifts[-1] != center.closing:
        shifts.append(fo(shifts[-1]))
    return shifts

def get_shifts_blocks_avalaible(center_id, date1=date.today()):
    """Retorna los bloques de horario disponibles para el día date1, para un centro dado"""

    center = Center.get_by_id(center_id)
    if center is None:
        raise ValueError("Error al obtener el centro id={}".format(center_id))
    shifts = center.get_shifts_by_date(date1)
    if shifts:
        not_avalaible = list(map(lambda s: (s.start_time if s.start_time in shift_time_blocks else None), shifts))
        return [t for t in shift_time_blocks if t not in not_avalaible]  # shift_time_blocks - not_avalaible
    return shift_time_blocks


class Shifts(Base):
    __tablename__ = 'shifts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    donor_email = Column(String, nullable=False, index=True)
    donor_phone = Column(String)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    date = Column(Date, nullable=False)
    center_id = Column(Integer, ForeignKey('centers.id'))

    def __init__(self, donor_email, donor_phone, start_time, end_time, date, center_id):
        self.donor_email = donor_email
        self.donor_phone = donor_phone
        self.start_time = start_time
        self.end_time = end_time
        self.date = date
        self.center_id = center_id

    def __repr__(self):
        return "<Shift(id='{}', start_time='{}', end_time='{}', center={})'>".format(self.id, self.start_time,
                                                                                     self.end_time, self.center.name)

    @classmethod
    def all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, shift_id):
        return cls.query.get(shift_id)

    @classmethod
    def search_by_center_name(cls, center_name):
        """Este método devuelve una lista con todos los turnos pertenecientes a un centro 'center_name'
        Si no se encuentran turnos devuelve una lista vacía"""
        return cls.query.filter(Center.name == center_name).all()

    @classmethod
    def search_by_center_name_like(cls, search_name):
        """Este método devuelve una lista con todos los turnos pertenecientes a un centro, o centros que
        contengan 'search_name' en su nombre. Si no se encuentran turnos devuelve una lista vacía"""

        return cls.query.filter(Center.name.like("%{}%".format(search_name))).all()

    @classmethod
    def search_by_center_id(cls, center_id):
        """Este método devuelve una lista con todos los turnos pertenecientes a un centro con id 'center_id'
        Si no se encuentran turnos devuelve una lista vacía"""
        return cls.query.filter(cls.center_id == center_id).all()

    @classmethod
    def search_by_donor_email(cls, donor_email):
        """Este método devuelve una lista con todos los turnos pertenecientes a una persona con email 'donor_email'
        Si no se encuentran turnos devuelve una lista vacía"""
        return cls.query.filter(cls.donor_email == donor_email).all()

    @classmethod
    def query_donor_email(cls, donor_email):
        """Este método devuelve una Shift.query con todos los turnos pertenecientes a una persona con email 'donor_email'"""
        return cls.query.filter(cls.donor_email == donor_email)

    @classmethod
    def query_center_name(cls, center_name):
        """Este método devuelve una Shift.query con todos los turnos pertenecientes a una persona con email 'donor_email'"""
        return cls.query.filter(Center.name == center_name)

    @classmethod
    def get_shifts_between(cls, date1=None, date2=None):
        """
        Devuelve los turnos con fechas entre date1 y date2.
        Si no se reciben fechas devuelve los turnos de hoy y los siguientes 2 días
        Valores por defecto: date1=date.today(), date2=date.today()+ 2 days
        """
        if date1 is None:
            date1 = date.today()
        if date2 is None:
            date2 = (datetime.now() + timedelta(2)).date()

        return cls.query.filter(cls.date >= date1).filter(cls.date <= date2).all()

    @classmethod
    def query_shifts_between(cls, date1=None, date2=None):
        """
        Devuelve una Query con los turnos con fechas entre date1 y date2.
        Si no se reciben fechas devuelve una Query con turnos de hoy y los siguientes 2 días
        Valores por defecto: date1=date.today(), date2=date.today()+ 2 days
        """
        if date1 is None:
            date1 = date.today()
        if date2 is None:
            date2 = (datetime.now() + timedelta(2)).date()

        return cls.query.filter(cls.date >= date1).filter(cls.date <= date2)

    def serialize(self):
        return {
            'id': self.id,
            'donor_email': self.donor_email,
            'donor_phone': self.donor_phone,
            'start_time': self.start_time.__str__(),
            'end_time': self.end_time.__str__(),
            'date': self.date.__str__(),
            'center': self.center.name,
        }

    # def serialize(self):
    #     return json.dumps(self._to_dict(), default=str, indent=4, sort_keys=True)
