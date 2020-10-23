from sqlalchemy.orm import relationship

from app.db import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, LargeBinary, ForeignKey
from datetime import datetime


class Center(Base):
    __tablename__ = 'centers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    address = Column(String(), nullable=True)
    phone = Column(String())
    email = Column(String(25), nullable=False)
    web_site = Column(String())
    opening = Column(DateTime())
    closing = Column(DateTime())
    published = Column(Boolean(), default=False)
    geo_location = Column(String(50))
    protocol = Column(LargeBinary())
    city_id = Column(Integer, ForeignKey('city.id'))
    type_id = Column(Integer, ForeignKey('centerType.id'))

    def __init__(self, name=None, address=None, phone=None, email=None, opening=None, closing=None):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.opening = opening
        self.closing = closing

    def __update__(self):
        self.update_date = datetime.now()

    def register_update(self):
        self.__update__()

    def __repr__(self):
        return "<Center(name='{}')'>".format(self.name, self.id)
