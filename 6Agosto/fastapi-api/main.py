from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="API Productos - FastAPI")


class Producto(BaseModel):
    id: int
    nombre: str
    precio: float


class ProductoCrear(BaseModel):
    nombre: str
    precio: float


productos = [
    Producto(id=1, nombre="Laptop", precio=2500000),
    Producto(id=2, nombre="Mouse", precio=45000),
    Producto(id=3, nombre="Teclado", precio=120000)
]


@app.get("/productos", response_model=List[Producto])
def listar_productos():
    return productos


@app.get("/productos/{producto_id}", response_model=Producto)
def obtener_producto(producto_id: int):
    for p in productos:
        if p.id == producto_id:
            return p
    raise HTTPException(
        status_code=404,
        detail="Producto no encontrado"
    )


@app.post("/productos", response_model=Producto, status_code=201)
def crear_producto(producto: ProductoCrear):
    nuevo = Producto(
        id=len(productos) + 1,
        nombre=producto.nombre,
        precio=producto.precio
    )
    productos.append(nuevo)
    return nuevo


@app.put("/productos/{producto_id}", response_model=Producto)
def actualizar_producto(producto_id: int, producto: ProductoCrear):
    for p in productos:
        if p.id == producto_id:
            p.nombre = producto.nombre
            p.precio = producto.precio
            return p
    raise HTTPException(
        status_code=404,
        detail="Producto no encontrado"
    )


@app.delete("/productos/{producto_id}", response_model=Producto)
def eliminar_producto(producto_id: int):
    for i, p in enumerate(productos):
        if p.id == producto_id:
            return productos.pop(i)
    raise HTTPException(
        status_code=404,
        detail="Producto no encontrado"
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)