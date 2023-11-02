from .database import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship


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

class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    path_id = Column(Integer, ForeignKey("paths.id"), nullable=False)
    path = relationship("Path")
    rarity = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("NOW()"))
    element_id = Column(Integer, ForeignKey("elements.id"), nullable=False)
    element = relationship("Element")

class LightCone(Base):
    __tablename__ = "light_cones"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    icon = Column(String, nullable=False)
    atk = Column(Integer, nullable=False)
    hp = Column(Integer, nullable=False)
    defence = Column(Integer, nullable=False)
    rarity = Column(Integer, nullable=False)
    path_id = Column(Integer, ForeignKey("paths.id"), nullable=False)
    path = relationship("Path")
    image = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("NOW()"))
