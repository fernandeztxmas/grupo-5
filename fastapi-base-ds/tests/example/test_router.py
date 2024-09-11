import pytest
from typing import Union
from sqlalchemy.orm import Session
from fastapi.testclient import TestClient
from fastapi import status
from tests.database import app, session
from src.example.exceptions import ErrorCode


client = TestClient(app)


def test_read_personas(session: Session) -> None:
    response = client.get(f"/personas")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 2


def test_read_mascotas(session: Session) -> None:
    response = client.get(f"/mascotas")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 3
