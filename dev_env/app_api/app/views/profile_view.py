from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException, status


from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.responses import Response

from pydantic import parse_obj_as
from typing import List, Union

from sqlalchemy.orm import Session
from app.services.db_services import get_db

from app.models.user_model import UserModel

from app.services.user_services import get_current_user

from app.schemas.profile_schema import ProfileUpdateSchema, ProfileCreateSchema, ProfileSchema

from app.services.profile_services import get_profile_by_id_service, create_profile_service,\
    delete_profile_service, get_all_profiles_service, update_profile_service


router_profile = APIRouter(
    prefix="/profile"
)


@router_profile.get("/", response_model=ProfileSchema)
def list_patients(db: Session = Depends(get_db),
                  user: UserModel = Depends(get_current_user)):

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuário não está autenticado"
        )

    profile_list = parse_obj_as(List[ProfileSchema], get_all_profiles_service(db))
    return JSONResponse(jsonable_encoder(profile_list))


@router_profile.get("/{profile_id}", response_model=ProfileSchema)
def get_person(profile_id: int, db: Session = Depends(get_db),
               user: UserModel = Depends(get_current_user)) -> ProfileSchema:

    if not user:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail="Usuário não está autenticado"
        )

    if profile := get_profile_by_id_service(db, profile_id):
        return profile

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=" Não foi possível acessar os dados solicitados."
    )


@router_profile.post("/", response_model=ProfileSchema)
def create_profile(profile_data: ProfileCreateSchema, db: Session = Depends(get_db)):
    if new_profile := create_profile_service(db, profile_data):
        return new_profile

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Não foi possível criar um perfil com os dados fornecidos."
    )


@router_profile.patch("/{profile_id}", response_model=ProfileSchema)
def update_person(profile_id: int, update_data: ProfileUpdateSchema,
                  db: Session = Depends(get_db), user: UserModel = Depends(get_current_user)) -> ProfileSchema:

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuário não está autenticado."
        )

    if person_update := update_profile_service(db, profile_id, update_data):
        return person_update

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Não foi possível atualizar o seu perfil com os dados informados, por favor verifique e tente novamente."
    )


@router_profile.delete("/{profile_id}", status_code=HTTPStatus.NO_CONTENT)
def delete_person(profile_id: int, db: Session = Depends(get_db),
                  user: UserModel = Depends(get_current_user)) -> Response:

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuário não está autenticado."
        )

    if not delete_profile_service(db, profile_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Não foi possível deletar o perfil solicitado."
        )

    return Response(
        status_code=HTTPStatus.NO_CONTENT.value
    )
