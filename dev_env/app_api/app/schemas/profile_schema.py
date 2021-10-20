from typing import Optional, List
from pydantic import Field

from app.schemas.user_schema import UserSchema
from app.schemas.base_schema import BaseMD


class ProfileCreateSchema(BaseMD):
    profile_url: str
    banner_profile_url: str
    bio: str
    user_id: Optional[int] = None


class ProfileUpdateSchema(BaseMD):
    profile_url: Optional[str] = ""
    banner_profile_url: Optional[str] = ""
    bio: Optional[str]
    user_id: Optional[int] = None


class ProfileSchema(BaseMD):
    id: int
    profile_url: str
    banner_profile_url: str
    bio: str
    user: Optional[UserSchema] = Field(...)

    class Config:
        orm_mode = True
