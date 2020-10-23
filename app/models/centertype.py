from sqlalchemy.orm import relationship

from app.db import Base
from sqlalchemy import Column, Integer, String


class CenterType(Base):
    __tablename__ = 'centerType'
    id = Column(Integer, primary_key=True)
    description = Column(String(50))
    type_centers = relationship(
        'Center',
        backref="type")

    def __init__(self, description):
        self.description = description

    def __repr__(self):
        return "<CenterType(description={}, id={})>".format(self.description, self.id)