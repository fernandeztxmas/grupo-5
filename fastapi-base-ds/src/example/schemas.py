#from pydantic import BaseModel, EmailStr, field_validator
#from typing import List
#from datetime import datetime
#from src.example.models import TipoMascota
#from src.example.constants import ErrorCode
#from src.example import exceptions *#

# Los siguientes schemas contienen atributos sin muchas restricciones de tipo.
# Podemos crear atributos con ciertas reglas mediante el uso de un "Field" adecuado.
# https://docs.pydantic.dev/latest/concepts/fields/


from pydantic import BaseModel, EmailStr, field_validator
from typing import List
from datetime import datetime

# Clase base Producto
class ProductoBase(BaseModel):
    nombre: str
    precio: float
    descripcion: str
   # fecha_creacion: datetime = Field(default_factory=datetime.now)
   # fecha_modificacion: datetime = Field(default_factory=datetime.now)

    class Config:
        from_attributes = True

# Clases de creación y actualización de Producto
class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(ProductoBase):
    pass

class Producto(ProductoBase):
    id: int

# Clase para Pizzas extendiendo de ProductoBase
class PizzaBase(ProductoBase):
    ingredientes: List[str]
    tamaño: str  # pequeño, mediano, grande

class PizzaCreate(PizzaBase):
    id: int
    nombre: str
    precio: float
    descripcion: str

class PizzaUpdate(PizzaBase):
    pass

class Pizza(PizzaBase):
    id: int

# Clase para Zapatos extendiendo de ProductoBase
class ZapatoBase(ProductoBase):
    talla: int
    color: str
    material: str

class ZapatoCreate(ZapatoBase):
    pass

class ZapatoUpdate(ZapatoBase):
    pass

class Zapato(ZapatoBase):
    id: int
