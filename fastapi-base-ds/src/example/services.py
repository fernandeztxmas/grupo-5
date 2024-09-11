from typing import List
from sqlalchemy.orm import Session
from src.example.models import Producto, Pizza, Zapato
from src.example import schemas, exceptions

def crear_producto(db: Session, producto: schemas.ProductoCreate) -> Producto:
    db_producto = Producto(
        nombre=producto.nombre,
        precio=producto.precio,
        descripcion=producto.descripcion
    )
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

def listar_productos(db: Session) -> List[Producto]:
    return db.query(Producto).all()

def leer_producto(db: Session, producto_id: int) -> Producto:
    db_producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if db_producto is None:
        raise exceptions.ProductoNoEncontrado()
    return db_producto

def modificar_producto(
    db: Session, producto_id: int, producto: schemas.ProductoUpdate
) -> Producto:
    db_producto = leer_producto(db, producto_id)
    if producto.nombre:
        db_producto.nombre = producto.nombre
    if producto.precio is not None:
        db_producto.precio = producto.precio
    if producto.descripcion:
        db_producto.descripcion = producto.descripcion
    db.commit()
    db.refresh(db_producto)
    return db_producto

def eliminar_producto(db: Session, producto_id: int) -> Producto:
    db_producto = leer_producto(db, producto_id)
    db.delete(db_producto)
    db.commit()
    return db_producto


# Operaciones CRUD para Pizzas


from sqlalchemy.orm import Session
from . import schemas, models

def crear_pizza(db: Session, pizza: schemas.PizzaCreate) -> models.Pizza:
    # Verificamos que el producto existe antes de crear la pizza
    db_producto = leer_producto(db, pizza.id)
    db_pizza = models.Pizza(
        nombre=pizza.nombre,
        precio=pizza.precio,
        descripcion=pizza.descripcion,
        ingredientes=pizza.ingredientes, 
        tamaño=pizza.tamaño,
        producto_id=pizza.id
    )
    db.add(db_pizza)
    db.commit()
    db.refresh(db_pizza)
    return db_pizza


def listar_pizzas(db: Session) -> List[Pizza]:
    return Pizza.get_all(db)


def leer_pizza(db: Session, pizza_id: int) -> Pizza:
    db_pizza = Pizza.get(db, pizza_id)
    if db_pizza is None:
        raise exceptions.PizzaNoEncontrada()
    return db_pizza


def modificar_pizza(
    db: Session, pizza_id: int, pizza: schemas.PizzaUpdate
) -> Pizza:
    db_pizza = leer_pizza(db, pizza_id)
    return db_pizza.update(
        db,
        ingredientes=",".join(pizza.ingredientes),
        tamaño=pizza.tamaño,
    )


def eliminar_pizza(db: Session, pizza_id: int) -> Pizza:
    db_pizza = leer_pizza(db, pizza_id)
    db_pizza.delete(db)
    return db_pizza


# Operaciones CRUD para Zapatos


def crear_zapato(db: Session, zapato: schemas.ZapatoCreate) -> Zapato:
    # Verificamos que el producto existe antes de crear el zapato
    db_producto = leer_producto(db, zapato.producto_id)
    return Zapato.create(
        db,
        producto_id=db_producto.id,
        talla=zapato.talla,
        color=zapato.color,
        material=zapato.material,
    )


def listar_zapatos(db: Session) -> List[Zapato]:
    return Zapato.get_all(db)


def leer_zapato(db: Session, zapato_id: int) -> Zapato:
    db_zapato = Zapato.get(db, zapato_id)
    if db_zapato is None:
        raise exceptions.ZapatoNoEncontrado()
    return db_zapato


def modificar_zapato(
    db: Session, zapato_id: int, zapato: schemas.ZapatoUpdate
) -> Zapato:
    db_zapato = leer_zapato(db, zapato_id)
    return db_zapato.update(
        db,
        talla=zapato.talla,
        color=zapato.color,
        material=zapato.material,
    )


def eliminar_zapato(db: Session, zapato_id: int) -> Zapato:
    db_zapato = leer_zapato(db, zapato_id)
    db_zapato.delete(db)
    return db_zapato
