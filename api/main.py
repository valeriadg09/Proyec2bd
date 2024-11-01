from fastapi import FastAPI
from .endpoints import clientes, productos, proveedores, pedidos, consultas, populate_endpoints

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

app.include_router(clientes.router, prefix="/clientes", tags=["clientes"])
app.include_router(productos.router, prefix="/productos", tags=["productos"])
app.include_router(proveedores.router, prefix="/proveedores", tags=["proveedores"])
app.include_router(pedidos.router, prefix="/pedidos", tags=["pedidos"])
app.include_router(consultas.router, prefix="/consultas", tags=["consultas"])
app.include_router(populate_endpoints.router, prefix="/populate", tags=["populate"])
