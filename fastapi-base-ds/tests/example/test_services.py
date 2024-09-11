import pytest
from typing import Union
from sqlalchemy.orm import Session
from fastapi.testclient import TestClient
from fastapi import status
from tests.database import app, session
from src.example import exceptions
from src.example.services import (
    listar_personas,
    listar_mascotas,
    crear_persona,
    modificar_persona,
    leer_persona,
    eliminar_persona
)
from src.example.schemas import PersonaCreate, PersonaUpdate


def test_crear_persona(session: Session) -> None:
    nombre = "Pepe"
    email = "pepe@gmail.com"
    persona_3 = crear_persona(session, PersonaCreate(nombre=nombre, email=email))
    assert persona_3.nombre == nombre
    assert persona_3.email == email


def test_modificar_persona(session: Session) -> None:
    nuevo_nombre = "Pepe"
    persona_id = 2
    persona_2 = leer_persona(session, persona_id)
    assert persona_2.nombre == "Ana"
    persona_2 = modificar_persona(
        session, persona_id, PersonaUpdate(nombre=nuevo_nombre, email=persona_2.email)
    )
    assert persona_2.nombre == nuevo_nombre

def test_eliminar_persona(session: Session) -> None:

    # intentamos borrar a una persona con mascotas.
    # verificamos que se lanza la excepcion esperada
    with pytest.raises(exceptions.PersonaTieneMascotas):
        persona_id = 2
        persona_2 = eliminar_persona(session, persona_id)

    # probamos crear una persona nueva y eliminarla.
    nombre = "Pepe"
    email = "pepe@gmail.com"
    persona_3 = crear_persona(session, PersonaCreate(nombre=nombre, email=email))

    personas = listar_personas(session)
    assert len(personas) == 3

    persona_3 = eliminar_persona(session, persona_3.id)

    personas = listar_personas(session)
    assert len(personas) == 2


def test_listar_personas(session: Session) -> None:
    personas = listar_personas(session)
    assert len(personas) == 2


def test_listar_mascotas(session: Session) -> None:
    mascotas = listar_mascotas(session)
    assert len(mascotas) == 3
