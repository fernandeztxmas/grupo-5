from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import get_db
from src.example import models, schemas, exceptions, services

router = APIRouter()

@router.post("/productos", response_model=schemas.Producto)
def create_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    return services.crear_producto(db, producto)

@router.get("/productos", response_model=list[schemas.Producto])
def read_productos(db: Session = Depends(get_db)):
    return services.listar_productos(db)

@router.get("/productos/{producto_id}", response_model=schemas.Producto)
def read_producto(producto_id: int, db: Session = Depends(get_db)):
    return services.leer_producto(db, producto_id)

@router.put("/productos/{producto_id}", response_model=schemas.Producto)
def update_producto(
    producto_id: int, producto: schemas.ProductoUpdate, db: Session = Depends(get_db)
):
    return services.modificar_producto(db, producto_id, producto)

@router.delete("/productos/{producto_id}", response_model=schemas.Producto)
def delete_producto(producto_id: int, db: Session = Depends(get_db)):
    return services.eliminar_producto(db, producto_id)


# Rutas para Pizzas

@router.post("/pizzas", response_model=schemas.Pizza)
def create_pizza(pizza: schemas.PizzaCreate, db: Session = Depends(get_db)):
    return services.crear_pizza(db, pizza)


@router.get("/pizzas", response_model=list[schemas.Pizza])
def read_pizzas(db: Session = Depends(get_db)):
    return services.listar_pizzas(db)


@router.get("/pizzas/{pizza_id}", response_model=schemas.Pizza)
def read_pizza(pizza_id: int, db: Session = Depends(get_db)):
    return services.leer_pizza(db, pizza_id)


@router.put("/pizzas/{pizza_id}", response_model=schemas.Pizza)
def update_pizza(
    pizza_id: int, pizza: schemas.PizzaUpdate, db: Session = Depends(get_db)
):
    return services.modificar_pizza(db, pizza_id, pizza)


@router.delete("/pizzas/{pizza_id}", response_model=schemas.Pizza)
def delete_pizza(pizza_id: int, db: Session = Depends(get_db)):
    return services.eliminar_pizza(db, pizza_id)


# Rutas para Zapatos

@router.post("/zapatos", response_model=schemas.Zapato)
def create_zapato(zapato: schemas.ZapatoCreate, db: Session = Depends(get_db)):
    return services.crear_zapato(db, zapato)


@router.get("/zapatos", response_model=list[schemas.Zapato])
def read_zapatos(db: Session = Depends(get_db)):
    return services.listar_zapatos(db)


@router.get("/zapatos/{zapato_id}", response_model=schemas.Zapato)
def read_zapato(zapato_id: int, db: Session = Depends(get_db)):
    return services.leer_zapato(db, zapato_id)


@router.put("/zapatos/{zapato_id}", response_model=schemas.Zapato)
def update_zapato(
    zapato_id: int, zapato: schemas.ZapatoUpdate, db: Session = Depends(get_db)
):
    return services.modificar_zapato(db, zapato_id, zapato)


@router.delete("/zapatos/{zapato_id}", response_model=schemas.Zapato)
def delete_zapato(zapato_id: int, db: Session = Depends(get_db)):
    return services.eliminar_zapato(db, zapato_id)
