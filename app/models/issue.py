from app.db import Base
from sqlalchemy import Column, Integer, String
import json


class Issue(Base):
    __tablename__ = 'issues'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    description = Column(String)
    category_id = Column(String)
    status_id = Column(String)

    def __init__(self, email=None, description=None, category_id=None, status_id=None):
        self.email = email
        self.description = description
        self.category_id = category_id
        self.status_id = status_id

    def __repr__(self):
        return "<Issue(email='{}', id='{}')>".format(self.email, self.id)

    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'description': self.description,
            'category_id': self.category_id,
            'status_id': self.status_id
        }
    #
    # def serialize(self):
    #     return json.dumps(self._to_dict(), indent=4, sort_keys=True, default=str)
