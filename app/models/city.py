from sqlalchemy.orm import relationship

from app.db import Base
from sqlalchemy import Column, Integer, String


class City(Base):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    city_centers = relationship(
        'Center',
        backref="city")

    def __init__(self, description):
        self.name = description

    def __repr__(self):
        return "<City(name={}, id={})>".format(self.name, self.id)