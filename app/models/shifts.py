from app.db import Base
from sqlalchemy import Column, Integer, ForeignKey, String, Time, Date
from sqlalchemy.orm import relationship


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
        return "<Shift(id='{}', start_time='{}', end_time='{}')'>".format(self.start_time, self.end_time, self.id)
