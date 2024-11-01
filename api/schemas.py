from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class ClienteBase(BaseModel):
    nombre: str
    apellido: str
    email: str
    telefono: str

class ClienteCreate(ClienteBase):
    pass

class Cliente(ClienteBase):
    id: int
    pedidos: List['Pedido'] = []

    class Config:
        from_attributes = True

class ProductoBase(BaseModel):
    nombre: str
    descripcion: str
    precio: float

class ProductoCreate(ProductoBase):
    pass

class Producto(ProductoBase):
    id: int

    class Config:
        from_attributes = True

class PedidoBase(BaseModel):
    cliente_id: int
    fecha: date

class PedidoCreate(PedidoBase):
    pass

class Pedido(PedidoBase):
    id: int
    detalles: List['DetallePedido'] = []

    class Config:
        from_attributes = True

class DetallePedidoBase(BaseModel):
    pedido_id: int
    producto_id: int
    cantidad: int
    precio: float

class DetallePedidoCreate(DetallePedidoBase):
    pass

class DetallePedido(DetallePedidoBase):
    id: int

    class Config:
        from_attributes = True

class ProveedorBase(BaseModel):
    nombre: str
    telefono: str
    email: str

class ProveedorCreate(ProveedorBase):
    pass

class Proveedor(ProveedorBase):
    id: int

    class Config:
        from_attributes = True

class ProductoProveedorBase(BaseModel):
    producto_id: int
    proveedor_id: int

class ProductoProveedorCreate(ProductoProveedorBase):
    pass

class ProductoProveedor(ProductoProveedorBase):
    id: int

    class Config:
        from_attributes = True
