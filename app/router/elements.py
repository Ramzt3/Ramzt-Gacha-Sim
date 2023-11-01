from typing import List
from fastapi import APIRouter, status, Response, HTTPException, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas

router = APIRouter(
    prefix="/elements",
    tags=["elements"]
)

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.ElementRes])
def get_elem(db: Session = Depends(get_db)):
    element = db.query(models.Element).all()
    if not element:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Elements does not exist")
    
    return element

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ElementRes)
def create_elem(data: schemas.ElementCreate, db: Session = Depends(get_db)):
    new_elem = models.Element(**data.model_dump())
    db.add(new_elem)
    db.commit()
    db.refresh(new_elem)

    return new_elem

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_elem(id: int,db: Session = Depends(get_db)):
    elem = db.query(models.Element).filter(models.Element.id == id)
    if not elem.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Element does not exist")

    elem.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ElementRes)
def edit_elem(id: int, data: schemas.ElementBase, db: Session = Depends(get_db)):
    elem = db.query(models.Element).filter(models.Element.id == id)
    if not elem.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Element does not exist")

    elem.update(data.model_dump(), synchronize_session=False)
    db.commit()

    return elem.first()
