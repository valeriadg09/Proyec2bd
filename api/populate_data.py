import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.orm import Session
from api import models, schemas, crud
from api.database import SessionLocal

def populate_clientes(db: Session):
    clientes = [
        {"nombre": "Juan", "apellido": "Pérez", "email": "juan.perez@example.com", "telefono": "123456789"},
        {"nombre": "María", "apellido": "García", "email": "maria.garcia@example.com", "telefono": "987654321"},
        {"nombre": "Luis", "apellido": "Martínez", "email": "luis.martinez@example.com", "telefono": "654321987"}
    ]
    for cliente_data in clientes:
        cliente = schemas.ClienteCreate(**cliente_data)
        crud.create_cliente(db=db, cliente=cliente)

def populate_productos(db: Session):
    productos = [
        {"nombre": "Producto A", "descripcion": "Descripción del producto A", "precio": 10.99},
        {"nombre": "Producto B", "descripcion": "Descripción del producto B", "precio": 20.50},
        {"nombre": "Producto C", "descripcion": "Descripción del producto C", "precio": 30.00}
    ]
    for producto_data in productos:
        producto = schemas.ProductoCreate(**producto_data)
        crud.create_producto(db=db, producto=producto)

def populate_proveedores(db: Session):
    proveedores = [
        {"nombre": "Proveedor 1", "telefono": "123123123", "email": "proveedor1@example.com"},
        {"nombre": "Proveedor 2", "telefono": "456456456", "email": "proveedor2@example.com"}
    ]
    for proveedor_data in proveedores:
        proveedor = schemas.ProveedorCreate(**proveedor_data)
        crud.create_proveedor(db=db, proveedor=proveedor)

def populate_data():
    db = SessionLocal()
    try:
        populate_clientes(db)
        populate_productos(db)
        populate_proveedores(db)
    finally:
        db.close()

if __name__ == "__main__":
    populate_data()
