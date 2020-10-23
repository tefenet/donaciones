from sqlalchemy.orm import relationship

from app.db import Base
from sqlalchemy import Column, Integer, String


class City(Base):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True)
    description = Column(String(50))
    city_centers = relationship(
        'Center',
        backref="city")

    def __init__(self, description):
        self.description = description

    def __repr__(self):
        return "<City(description={}, id={})>".format(self.description, self.id)