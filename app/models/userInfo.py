from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, BIGINT, Text, INT, DATETIME

Base = declarative_base()


class User(Base):
    __tablename__ = 'userinfo'
    id = Column(BIGINT, primary_key=True, autoincrement=True)
    account = Column(Text, nullable=False)
    username = Column(Text, nullable=True)
    password = Column(Text, nullable=False)
    phone = Column(Text, nullable=False)
    age = Column(INT, nullable=True)
    createdTime = Column(Text, nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
