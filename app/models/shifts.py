from sqlalchemy import Column, Integer, ForeignKey, String, Time, Date
from datetime import datetime, timedelta, date, time
from app.helpers.pagination import paginate
from app.models.sistema import Sistema
from app.db import Base, dbSession
from flask import flash


# from app.models.center import Center


class Shifts(Base):
    __tablename__ = 'shifts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    donor_email = Column(String, nullable=False, index=True)
    donor_phone = Column(String)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    date = Column(Date, nullable=False)
    center_id = Column(Integer, ForeignKey('centers.id'))

    def __init__(self, donor_email=None, donor_phone=None, start_time=None, end_time=None, shift_date=None,
                 center_id=None):
        self.donor_email = donor_email
        self.donor_phone = donor_phone
        self.start_time = start_time
        self.end_time = end_time
        self.date = shift_date
        self.center_id = center_id

    def __repr__(self):
        return "<Shift(id='{}', start_time='{}', end_time='{}', center_id={})'>".format(self.id, self.start_time,
                                                                                        self.end_time, self.center_id)

    @classmethod
    def available_shifts(cls, center, shifts=[]):
        """Este método devuelve una lista con todos los horarios de turnos disponibles de un centro
            recibe los turnos reservados de un dia para un centro x, y recibe el centro x"""
        if shifts:
            start_not_available = list(map(lambda s: s.start_time, shifts))
            return list(filter(lambda sh: sh not in start_not_available, cls.shift_time_block(center)))
        return cls.shift_time_block(center)

    @classmethod
    def shift_time_block(cls, center):
        """Este método devuelve una lista con todos los horarios de turnos por dia de un centro
        de acuerdo a su horario de apertura y cierre"""
        shifts = [center.opening]

        def add_30_minutes(t):
            return (datetime(1, 1, 1, t.hour, t.minute) + timedelta(minutes=30)).time()

        while shifts[-1] < center.closing:
            shifts.append(add_30_minutes(shifts[-1]))
        return shifts[:-1]

    @classmethod
    def all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, shift_id):
        return cls.query.get(shift_id)

    # @classmethod
    # def search_by_center_name(cls, center_name):
    #     """Este método devuelve una lista con todos los turnos pertenecientes a un centro 'center_name'
    #     Si no se encuentran turnos devuelve una lista vacía"""
    #     return cls.query.filter(Center.name == center_name).all()

    # @classmethod
    # def search_by_center_name_like(cls, search_name):
    #     """Este método devuelve una lista con todos los turnos pertenecientes a un centro, o centros que
    #     contengan 'search_name' en su nombre. Si no se encuentran turnos devuelve una lista vacía"""
    #
    #     return cls.query.filter(Center.name.like("%{}%".format(search_name))).all()

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
    def query_center_name(cls, c):
        """Este método devuelve una Shift.query con todos los turnos pertenecientes a una persona con email 'donor_email'"""
        return cls.query.filter(cls.center == c)

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

    @classmethod
    def delete_by_id(cls, shift_id):
        """Elimina un turno de la base de datos de forma permanente"""
        return cls.query.filter(cls.id == shift_id).delete()

    def serialize(self):
        return {
            'id': self.id,
            'donor_email': self.donor_email,
            'donor_phone': self.donor_phone,
            'start_time': self.start_time.__str__(),
            'end_time': self.end_time.__str__(),
            'date': self.date.__str__(),
            'center_id': self.center_id,
        }

    # def serialize(self):
    #     return json.dumps(self._to_dict(), default=str, indent=4, sort_keys=True)


def shift_avalaible(start_time, shifts_day):
    """Chequea si el turno esta disponible. Retorna un Boolean"""
    return list(filter(lambda s: s.start_time == start_time, shifts_day))


def get_end_time(start_time):
    t1 = datetime.strptime(str(start_time), '%H:%M:%S')
    t2 = datetime.strptime(str(time(0, 30)), '%H:%M:%S')
    time_zero = datetime.strptime(str(time(0)), '%H:%M:%S')
    return (t1 - time_zero + t2).time()


def create_shift(shift, center):
    """recibe un turno y un centro, lo valida antes de persistirlo."""
    if not center:
        flash("Error al obtener el Centro con ID {}".format(shift.center_id), "success")
    if center.valid_start_time(shift.start_time):
        available_start = center.get_shifts_blocks_avalaible(shift.date)
        if shift.start_time not in available_start:
            raise ValueError("Error: turno no disponible")
        shift.end_time = get_end_time(shift.start_time)
        dbSession.add(shift)
        dbSession.commit()
    else:
        raise ValueError("Franja horaria de turno no válida. El turno debe respetar la franja horaria de 9hs a 16hs.")


def search_by_donor_email_paginated(donor_email, page=1):
    """Retorna una paginación con los turnos que contengan donor_email"""
    sys = Sistema.get_sistema()
    query = Shifts.query_donor_email(donor_email)
    return paginate(query, page, sys.cant_por_pagina)


def search_by_center_name_paginated(center_name, page=1):
    """Retorna una paginación con los turnos pertenecientes al centro 'center_name'"""
    sys = Sistema.get_sistema()
    query = Shifts.query_center_name(center_name)
    return paginate(query, page, sys.cant_por_pagina)


def aval_shifts(center, shifts):
    return Shifts.available_shifts(center, shifts)
