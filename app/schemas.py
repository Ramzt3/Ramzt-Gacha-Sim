from typing import Union
from datetime import datetime
from pydantic import BaseModel

class ElementBase(BaseModel):
    name: str
    icon: str

class ElementCreate(ElementBase):
    pass
    
class ElementRes(ElementBase):
    id: int


class PathBase(BaseModel):
    name: str
    icon: str
class PathCreate(PathBase):
    pass

class PathRes(PathBase):
    id: int

class CharacterBase(BaseModel):
    name: str
    gender: str
    rarity: int
    element_id: int 
    path_id: int

class CharacterCreate(CharacterBase):
    pass

class CharacterRes(CharacterBase):
    id: int
    path: PathRes
    element: ElementRes
    created_at: datetime


class LightConeBase(BaseModel):
    name: str
    icon: str
    atk: int
    hp: int
    defence: int
    rarity: int
    path_id: int 
    image: str

class LightConeCreate(LightConeBase):
    pass

class LightConeRes(LightConeBase):
    id: int
    path: PathRes
    created_at: datetime
