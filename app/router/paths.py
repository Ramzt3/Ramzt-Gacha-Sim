
from typing import List
from fastapi import APIRouter, status, Response, HTTPException, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas

router = APIRouter(
    prefix="/paths",
    tags=["paths"]
)

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.PathRes])
def get_path(db: Session = Depends(get_db)):
    path = db.query(models.Path).all()
    if not path:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Path does not exist")
    
    return path

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.PathRes)
def create_path(data: schemas.PathCreate, db: Session = Depends(get_db)):
    new_path = models.Path(**data.model_dump())
    db.add(new_path)
    db.commit()
    db.refresh(new_path)

    return new_path

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_path(id: int, db: Session = Depends(get_db)):
    path = db.query(models.Path).filter(models.Path.id == id)
    if not path.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Path with id:{id} does not exist")

    path.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", status_code=status.HTTP_200_OK)
def edit_path(id: int, data: schemas.PathBase, db: Session = Depends(get_db)):
    path = db.query(models.Path).filter(models.Path.id == id)
    if not path.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Path with id:{id} does not exist")

    path.update(data.model_dump(), synchronize_session=False)
    db.commit()

    return path.first()
