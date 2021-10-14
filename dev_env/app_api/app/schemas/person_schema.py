from datetime import date
from typing import Optional
from pydantic import Field, validator

from app.schemas.base_schema import BaseMD
from app.services.documents_validation import cpf_validate


class PersonCreateSchema(BaseMD):
    cpf: str = Field(regex="[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}",
                     description="Sem caracter especial")

    name: str
    birth_date: date = None
    phone: str = Field("", regex="(\(?\d{2}\)?\s)?(\d{4,5}\-\d{4})",
                       description="Sem caracter especial")

    @validator('cpf')
    def cpf_is_a_valid_value(cls, value):
        if not cpf_validate(value):
            raise ValueError('CPF is not valid')
        return value


class PersonUpdateSchema(BaseMD):
    cpf: str = Field(regex="[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}",
                     description="Sem caracter especial")

    name: Optional[str] = ""
    birth_date: Optional[date] = None
    phone: Optional[str] = Field("", regex="(\(?\d{2}\)?\s)?(\d{4,5}\-\d{4})",
                       description="Sem caracter especial")

    @validator('cpf')
    def cpf_is_a_valid_value(cls, value):
        if cpf_validate(value):
            raise ValueError('CPF Invalido')
        return value


class PersonSchema(BaseMD):
    id: int
    cpf: str
    name: str
    birth_date: date = None
    phone: str

    class Config:
        orm_mode = True
