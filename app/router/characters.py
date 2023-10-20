from typing import List
from fastapi import APIRouter, status, Response, HTTPException, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas

router = APIRouter(
    prefix="/characters",
    tags=["characters"]
)

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.CharacterRes])
def get_char(db: Session = Depends(get_db)):
    char = db.query(models.Character).all()
    if not char:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Character does not exist")
    
    return char

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.CharacterRes)
def create_char(data: schemas.CharacterCreate, db: Session = Depends(get_db)):
    new_char = models.Character(**data.model_dump())
    db.add(new_char)
    db.commit()
    db.refresh(new_char)

    return new_char