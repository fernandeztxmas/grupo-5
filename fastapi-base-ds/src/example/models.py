from typing import Optional, List
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from enum import auto, StrEnum
from datetime import datetime, UTC
from src.models import BaseModel


class Persona(BaseModel):
    __tablename__ = "personas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    fecha_creacion: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(UTC))
    fecha_modificacion: Mapped[datetime] = mapped_column(
        DateTime, default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC)
    )
    mascotas: Mapped[Optional[List["Mascota"]]] = relationship(
        "Mascota", back_populates="tutor"
    )


class TipoMascota(StrEnum):
    GATO = auto()
    PERRO = auto()
    CONEJO = auto()
    COBAYO = auto()
    PEZ = auto()


class Mascota(BaseModel):
    __tablename__ = "mascotas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String, index=True)
    tipo: Mapped[TipoMascota] = mapped_column(String)  # e.g., "Gato", "Perro", etc.
    tutor_id: Mapped[int] = mapped_column(
        ForeignKey("personas.id")
    )  # Foreign key a Persona
    tutor: Mapped[Persona] = relationship("Persona", back_populates="mascotas")
    fecha_creacion: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(UTC))
    fecha_modificacion: Mapped[datetime] = mapped_column(
        DateTime, default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC)
    )

    @property
    def nombre_tutor(self):
        return self.tutor.nombre
