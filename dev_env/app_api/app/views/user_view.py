import jwt
import datetime
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.services.db_services import get_db
from app.schemas.user_schema import UserCreateSchema, UserSchema, UserUpdateSchema, UserPersonCreateSchema
from app.schemas.person_schema import PersonCreateSchema
from app.services.user_services import create_user_service, authenticate_user
from app.services.user_services import get_current_user, update_user_service
from app.services.person_services import create_new_person_service

from config import settings

router_user = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


@router_user.get("/users/me", response_model=UserSchema)
async def get_user(user=Depends(get_current_user)):

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='invalid credentials'
        )

    return user


@router_user.post("/token")
async def generate_token(login_form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = await authenticate_user(db, login_form.username, login_form.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Credenciais invalidas')

    user_schema = UserCreateSchema(username=user.username, password=user.password_hash, email=user.email,
                                   user_group=user.user_group,
                                   person_id=user.person_id)
    token = jwt.encode({"exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30), **user_schema.dict()},
                       settings["development"].SECRET_KEY)

    return {"access_token": token, "token_type": "bearer"}


@router_user.post("/users", response_model=UserSchema)
async def create_user(user: UserPersonCreateSchema, db: Session = Depends(get_db)):
    person_id = 0

    new_person = PersonCreateSchema(cpf=user.cpf,
                                    name=user.name,
                                    birth_date=user.birth_date,
                                    phone=user.phone)
    if person := create_new_person_service(db, new_person):
        person_id = person.id
        pass

    new_user = UserCreateSchema(username=user.username,
                                email=user.email,
                                password=user.password,
                                user_group=user.user_group,
                                person_id=person_id
                                )

    if new_user := create_user_service(db, new_user):
        print(new_user)
        return new_user

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )


@router_user.patch("/user/{user_id}", response_model=UserSchema)
async def update_user(user_id: int, new_user: UserUpdateSchema, db: Session = Depends(get_db)):
    if user := update_user_service(db, user_id, new_user):
        return user

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )
