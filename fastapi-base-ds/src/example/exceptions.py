from typing import Dict, Any, List, Union
from src.example.constants import ErrorCode
from src.exceptions import NotFound, BadRequest, PermissionDenied

class PersonaNoEncontrada(NotFound):
    DETAIL = ErrorCode.PERSONA_NO_ENCONTRADA


class MascotaNoEncontrada(NotFound):
    DETAIL = ErrorCode.MASCOTA_NO_ENCONTRADA


class EmailDuplicado(BadRequest):
    DETAIL = ErrorCode.EMAIL_DUPLICADO


class NombreDuplicado(BadRequest):
    DETAIL = ErrorCode.NOMBRE_DUPLICADO


class PersonaTieneMascotas(BadRequest):
    DETAIL = ErrorCode.PERSONA_TIENE_MASCOTAS

class TipoMascotaInvalido(ValueError):
    def __init__(self, posibles_tipos: List[str]):
        posibles_tipos = ", ".join(posibles_tipos)
        message = f"{ErrorCode.TIPO_MASCOTA_INVALIDO} {posibles_tipos}."
        super().__init__(message)
