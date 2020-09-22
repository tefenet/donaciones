from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Issue(Base):
    __tablename__ = 'issues'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    description = Column(String)
    category_id = Column(String)
    status_id = Column(String)

    def __repr__(self):
        return "<Issue(email='{}', id='{}')>".format(self.email, self.id)
