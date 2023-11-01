from .database import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship


class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    path = Column(String, nullable=False)
    rarity = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("NOW()"))
    element = Column(Integer, ForeignKey("elements.id"))

class Element(Base):
    __tablename__ = "elements"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    icon = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("NOW()"))

class Path(Base):
    __tablename__ = "paths"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    icon = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("NOW()"))
