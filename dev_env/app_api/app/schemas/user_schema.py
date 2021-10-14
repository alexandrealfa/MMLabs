from app.schemas.base_schema import BaseMD
from typing import Optional
from pydantic import Field
from app.schemas.person_schema import PersonSchema


class UserCreateSchema(BaseMD):
    username: str
    email: str
    password: str
    user_group: str
    person_id: Optional[int] = None


class UserPersonCreateSchema(BaseMD):
    name: str
    username: str
    cpf: str
    email: str
    phone: str
    birth_date: str
    user_group: str
    password: str


class UserUpdateSchema(BaseMD):
    username: Optional[str] = ""
    email: Optional[str] = ""
    last_password: Optional[str] = ""
    new_password: Optional[str] = ""
    user_group: Optional[str] = ""
    person_id: Optional[int] = None


class UserSchema(BaseMD):
    id: int
    username: str
    email: str
    user_group: str
    person: Optional[PersonSchema] = Field(...)

    class Config:
        orm_mode = True
