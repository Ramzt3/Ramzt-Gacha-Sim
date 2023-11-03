from typing import List
from fastapi import APIRouter, status, Response, HTTPException, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas

router = APIRouter(
    prefix="/light-cones",
    tags=["light-cones"]
)

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.LightConeRes])
def get_lcs(db: Session = Depends(get_db)):
    lc = db.query(models.LightCone).all()
    if not lc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Light Cone does not exist")
    
    return lc 

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.LightConeRes)
def get_lc(id: int, db: Session = Depends(get_db)):
    lc = db.query(models.LightCone).filter(models.LightCone.id == id).first()
    if not lc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Light Cone with id:{id} does not exist")
    
    return lc 

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.LightConeRes)
def create_lc(data: schemas.LightConeCreate, db: Session = Depends(get_db)):
    lc = models.LightCone(**data.model_dump())
    db.add(lc)
    db.commit()
    db.refresh(lc)

    return lc 

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_lc(id: int, db: Session = Depends(get_db)):
    lc = db.query(models.LightCone).filter(models.LightCone.id == id)
    if not lc.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Light Cone with id:{id} does not exist")

    lc.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", status_code=status.HTTP_200_OK)
def edit_lc(id: int, data: schemas.LightConeBase, db: Session = Depends(get_db)):
    lc = db.query(models.LightCone).filter(models.LightCone.id == id)
    if not lc.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Light Cone with id:{id} does not exist")

    lc.update(data.model_dump(), synchronize_session=False)
    db.commit()

    return lc.first()
