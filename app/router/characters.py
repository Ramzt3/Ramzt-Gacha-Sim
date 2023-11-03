from typing import List, Optional
from fastapi import APIRouter, status, Response, HTTPException, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas

router = APIRouter(
    prefix="/characters",
    tags=["characters"]
)

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.CharacterRes])
def get_chars(db: Session = Depends(get_db), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    char = db.query(models.Character).filter(models.Character.name.contains(search)).limit(limit).offset(skip).all()
    if not char:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Character does not exist")
    
    return char

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.CharacterRes)
def get_char(id: int, db: Session = Depends(get_db)):
    char = db.query(models.Character).filter(models.Character.id == id).first()
    if not char:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Character with id:{id} does not exist")
    
    return char

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.CharacterRes)
def create_char(data: schemas.CharacterCreate, db: Session = Depends(get_db)):
    new_char = models.Character(**data.model_dump())
    db.add(new_char)
    db.commit()
    db.refresh(new_char)

    return new_char

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_char(id: int, db: Session = Depends(get_db)):
    char = db.query(models.Character).filter(models.Character.id == id)
    if not char.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Character with id:{id} does not exist")

    char.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", status_code=status.HTTP_200_OK)
def edit_char(id: int, data: schemas.CharacterBase, db: Session = Depends(get_db)):
    char = db.query(models.Character).filter(models.Character.id == id)
    if not char.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Character with id:{id} does not exist")

    char.update(data.model_dump(), synchronize_session=False)
    db.commit()

    return char.first()
