import os
import pytest
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from typing import Generator
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import sessionmaker, Session
from src.main import app
from src.database import get_db
from src.models import BaseModel
from src.example.services import crear_persona, crear_mascota
from src.example.schemas import PersonaCreate, MascotaCreate
from src.example.models import TipoMascota

load_dotenv()

# creamos una db para testing
DATABASE_URL = os.getenv("DB_URL_TEST")
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    # utilizaremos esta funcion para "pisar" la que definimos en src/database.py.
    db = TestingSessionLocal()
    try:
        print("Using test DB!")
        yield db
    finally:
        db.close()

# forzamos a fastapi para que utilice la db para testing.
app.dependency_overrides[get_db] = override_get_db

@pytest.fixture
def session() -> Generator[Session, None, None]:
    # Creamos las tablas en la db de pruebas
    BaseModel.metadata.create_all(bind=engine)

    db = TestingSessionLocal()

    # aqui podemos crear instancias de objetos para hacer tests
    # haciendo uso de las funciones "create_<clase>" de services y los schemas <Clase>Create.
    persona_1 = crear_persona(db, PersonaCreate(nombre="Juan", email="juan.perez@gmail.com"))
    persona_2 = crear_persona(
        db, PersonaCreate(nombre="Ana", email="ana.dominguez@gmail.com")
    )
    mascota_1 = crear_mascota(db, MascotaCreate(nombre="Lola", tipo=TipoMascota.GATO, tutor_id=persona_1.id))
    mascota_2 = crear_mascota(db, MascotaCreate(nombre="Felipe", tipo=TipoMascota.PERRO, tutor_id=persona_1.id))
    mascota_3 = crear_mascota(db, MascotaCreate(nombre="Coco", tipo=TipoMascota.COBAYO, tutor_id=persona_2.id))

    # db.add_all(
    #     [
    #         persona_1,
    #         persona_2,
    #         mascota_1,
    #         mascota_2,
    #         mascota_3
    #     ]
    # )
    # db.commit()

    yield db

    db.close()
    BaseModel.metadata.drop_all(bind=engine)
