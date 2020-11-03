from app.db import Base
from sqlalchemy import Column, Integer, ForeignKey, String, Time, Date
from sqlalchemy.orm import relationship
from app.models.center import Center


class Shifts(Base):
    __tablename__ = 'shifts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    donor_email = Column(String, nullable=False, index=True)
    donor_phone = Column(String)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    date = Column(Date, nullable=False)
    center_id = Column(Integer, ForeignKey('centers.id'))
    center = relationship("Center", back_populates="shifts")

    def __init__(self, donor_email, donor_phone, start_time, end_time, date, center_id):
        self.donor_email = donor_email
        self.donor_phone = donor_phone
        self.start_time = start_time
        self.end_time = end_time
        self.date = date
        self.center_id = center_id

    def __repr__(self):
        return "<Shift(id='{}', start_time='{}', end_time='{}', center_id={})'>".format(self.id, self.start_time,
                                                                                        self.end_time, self.center.id)

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
