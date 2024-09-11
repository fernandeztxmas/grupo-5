from typing import List, Optional
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, UTC
from src.models import BaseModel


# Modelo base para productos
class Producto(BaseModel):
    __tablename__ = "productos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String, nullable=False, index=True)
    precio: Mapped[float] = mapped_column(Float, nullable=False)
    descripcion: Mapped[str] = mapped_column(String, nullable=True)
    fecha_creacion: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(UTC))
    fecha_modificacion: Mapped[datetime] = mapped_column(
        DateTime, default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC)
    )

    # Relación opcional para diferenciar entre pizzas y zapatos
    pizzas: Mapped[Optional[List["Pizza"]]] = relationship("Pizza", back_populates="producto", cascade="all, delete-orphan")
    zapatos: Mapped[Optional[List["Zapato"]]] = relationship("Zapato", back_populates="producto", cascade="all, delete-orphan")


# Modelo específico para pizzas
class Pizza(BaseModel):
    __tablename__ = "pizzas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    producto_id: Mapped[int] = mapped_column(ForeignKey("productos.id"), nullable=False)
    ingredientes: Mapped[str] = mapped_column(String, nullable=False)  # Los ingredientes se almacenan como string
    tamaño: Mapped[str] = mapped_column(String, nullable=False)  # pequeño, mediano, grande

    producto: Mapped[Producto] = relationship("Producto", back_populates="pizzas")


# Modelo específico para zapatos
class Zapato(BaseModel):
    __tablename__ = "zapatos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    producto_id: Mapped[int] = mapped_column(ForeignKey("productos.id"), nullable=False)
    talla: Mapped[int] = mapped_column(Integer, nullable=False)
    color: Mapped[str] = mapped_column(String, nullable=False)
    material: Mapped[str] = mapped_column(String, nullable=False)

    producto: Mapped[Producto] = relationship("Producto", back_populates="zapatos")
