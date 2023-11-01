from typing import Union
from datetime import datetime
from pydantic import BaseModel

class CharacterBase(BaseModel):
    name: str
    gender: str
    element: str
    path: str
    rarity: int

class CharacterCreate(CharacterBase):
    pass

class CharacterRes(CharacterBase):
    id: int
    created_at: datetime


class ElementBase(BaseModel):
    name: str
    icon: str

class ElementCreate(ElementBase):
    pass
    
class ElementRes(ElementBase):
    id: int
    created_at: datetime


class PathBase(BaseModel):
    name: str
    icon: str

class PathCreate(PathBase):
    pass

class PathRes(PathBase):
    id: int
    created_at: datetime
