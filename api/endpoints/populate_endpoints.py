from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..populate_data import populate_clientes, populate_productos, populate_proveedores

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/populate/clientes")
def populate_clientes_endpoint(db: Session = Depends(get_db)):
    populate_clientes(db)
    return {"message": "Clientes poblados exitosamente"}

@router.post("/populate/productos")
def populate_productos_endpoint(db: Session = Depends(get_db)):
    populate_productos(db)
    return {"message": "Productos poblados exitosamente"}

@router.post("/populate/proveedores")
def populate_proveedores_endpoint(db: Session = Depends(get_db)):
    populate_proveedores(db)
    return {"message": "Proveedores poblados exitosamente"}
