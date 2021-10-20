import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, ProgrammingError, DataError
from passlib.hash import bcrypt

from config import settings
from app.services.db_services import get_db
from app.schemas.user_schema import UserCreateSchema, UserSchema, UserUpdateSchema

from app.models.user_model import UserModel
from app.configurations.database import Base, engine

from typing import Union

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


def create_user_service(db: Session, new_user: UserCreateSchema) -> UserSchema:
    """
    This service create one new user in database
    :param db:
    :param new_user:
    :return:
    """
    try:
        Base.metadata.create_all(engine)
        current_user = new_user.dict()
        current_user["password_hash"] = bcrypt.hash(new_user.password)
        current_user.pop("password")
        db_user = UserModel(**current_user)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user

    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Não foi possível Criar o usuário. Verifique se os dados foram preenchidos corretamente."
        )

    except ProgrammingError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Não foi possível Criar o usuário, verifique se os dados foram preenchidos corretamente."
        )

    except DataError:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Dados Incorretos"
        )


async def authenticate_user(db: Session, email: str, password: str) -> Union[UserSchema, bool]:
    user = db.query(UserModel).filter(UserModel.email == email).first()
    if not user:
        return False
    if not user.verify_password(password):
        return False

    return user


async def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, settings["development"].SECRET_KEY, algorithms=['HS256'])
        user = db.query(UserModel).filter(UserModel.email == payload.get('email')).first()
        return user

    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='token expirado'
        )

    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='email e senha incorretos'
        )


def get_user_service(db: Session, user_id: int):
    """

    :param user_id:
    :param db:
    :return:
    """
    return db.query(UserModel).get(user_id)


def update_user_service(db: Session, user_id: int, new_user: UserUpdateSchema):
    """

    :param user_id:
    :param db:
    :param new_user:
    :return:
    """
    try:
        if current_user := get_user_service(db, user_id):
            user_updated = {
                key: value for key, value in new_user if value
            }
            if new_user.new_password and current_user.verify_password(new_user.last_password):
                user_updated['password_hash'] = bcrypt.hash(new_user.new_password)

            if new_user.new_password and not current_user.verify_password(new_user.last_password):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Senha incorreta."
                )

            if user_updated.get("last_password"):
                user_updated.pop("last_password")

            if user_updated.get("new_password"):
                user_updated.pop("new_password")

            db.query(UserModel).filter(UserModel.id == current_user.id).update(user_updated)
            db.commit()
            db.refresh(current_user)

            return current_user

    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Não foi possível Criar o usuário. Verifique se os dados foram preenchidos corretamente."
        )

    except ProgrammingError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Não foi possível Criar o usuário. Verifique se os dados foram preenchidos corretamente."
        )

    except DataError:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Dados Incorretos"
        )
