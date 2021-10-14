from datetime import date
from typing import Optional
from pydantic import Field, validator

from app.schemas.base_schema import BaseMD
from app.services.documents_validation import cpf_validate
from app.services.regex_validator_services import regex_validator


class PersonCreateSchema(BaseMD):
    cpf: str

    name: str
    birth_date: date = None
    phone: str

    @validator('cpf')
    def cpf_is_a_valid_value(cls, value):
        if not cpf_validate(value) or not regex_validator(value, "([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})"):
            raise ValueError('CPF is not valid')
        return value

    @validator('phone')
    def phone_is_valid(cls, value):
        if not regex_validator(value, "(\(?\d{2}\)?\s)?(\d{4,5}\-\d{4})"):
            raise ValueError('Phone is not valid')
        return value


class PersonUpdateSchema(BaseMD):
    cpf: str = Field("")

    name: Optional[str] = ""
    birth_date: Optional[date] = None
    phone: Optional[str] = Field("")

    @validator('cpf')
    def cpf_is_a_valid_value(cls, value):
        if not cpf_validate(value) or not regex_validator(value, "([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})"):
            raise ValueError('CPF is not valid')
        return value

    @validator('phone')
    def phone_is_valid(cls, value):
        if not regex_validator(value, "(\(?\d{2}\)?\s)?(\d{4,5}\-\d{4})"):
            raise ValueError('Phone is not valid')
        return value


class PersonSchema(BaseMD):
    id: int
    cpf: str
    name: str
    birth_date: date = None
    phone: str

    class Config:
        orm_mode = True
