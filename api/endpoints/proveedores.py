from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas
from ..database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[schemas.Proveedor])
def read_proveedores(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    proveedores = crud.get_proveedores(db, skip=skip, limit=limit)
    return proveedores

@router.post("/", response_model=schemas.Proveedor)
def create_proveedor(proveedor: schemas.ProveedorCreate, db: Session = Depends(get_db)):
    return crud.create_proveedor(db=db, proveedor=proveedor)
