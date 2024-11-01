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

# Ejemplo de consulta personalizada
@router.get("/max_precio_producto", response_model=float)
def max_precio_producto(db: Session = Depends(get_db)):
    max_precio = db.query(func.max(models.Producto.precio)).scalar()
    return max_precio

# Agrega más consultas aquí según sea necesario
