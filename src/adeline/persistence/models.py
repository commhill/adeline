"""
Persistence models
"""

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql.functions import now

Base = declarative_base()


class Group(Base):
    """
    A group of persons.
    """

    __tablename__ = "group"
    id = Column(Integer, primary_key=True)

    name = Column(String)


class Person(Base):
    """
    A person who can use the webapp
    """

    __tablename__ = "person"
    id = Column(Integer, primary_key=True)

    username = Column(String)
    created_on = Column(DateTime, default=now())

    group_id = Column(Integer, ForeignKey("group.id"))
    group = relationship(
        Group, backref=backref("groups", uselist=True, cascade="delete,all")
    )
