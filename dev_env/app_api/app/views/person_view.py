from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.responses import Response

from pydantic import parse_obj_as

from typing import List, Union

from sqlalchemy.orm import Session
from app.services.db_services import get_db
from app.services.person_services import get_person_service, create_new_person_service, get_all_person_service,\
    update_person_service, delete_person_service

from app.schemas.person_schema import PersonSchema, PersonCreateSchema, PersonCreateSchema, PersonUpdateSchema

from app.models.user_model import UserModel

from app.services.user_services import get_current_user


router_person = APIRouter(
    prefix="/person"
)


@router_person.get("/", response_model=PersonSchema)
def list_patients(db: Session = Depends(get_db)):
    person_list = parse_obj_as(List[PersonSchema], get_all_person_service(db))
    return JSONResponse(jsonable_encoder(person_list))


@router_person.get("/{current_id}", response_model=PersonSchema)
def get_current_person(current_id: int, db: Session = Depends(get_db),
                       user: UserModel = Depends(get_current_user)) -> PersonSchema:
    """
    This router return data by one person, with they id.
    :param user:
    :param current_id:
    :param db:
    :return:
    """

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Você não está autenticado."
        )

    if person := get_person_service(db, current_id):
        return person

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="O Id informado não está registrado em nosso banco de dados."
    )


@router_person.post("/", response_model=PersonSchema)
def create_person(new_person: PersonCreateSchema, db: Session = Depends(get_db)) -> PersonSchema:
    if person := create_new_person_service(db, new_person):
        return person

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Não foi possível criar um usuário com os dados fornecidos."
    )


@router_person.patch("/{person_id}", response_model=PersonSchema)
def update_person(person_id: int, update_data: PersonUpdateSchema,
                  db: Session = Depends(get_db), user: UserModel = Depends(get_current_user)) -> PersonSchema:

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Você não está autenticado."
        )

    if person_update := update_person_service(db, person_id, update_data):
        return person_update

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Não foi possível atualizar o seu perfil com os dados informados, por favor verifique e tente novamente."
    )


@router_person.delete("/{person_id}", status_code=HTTPStatus.NO_CONTENT)
def delete_person(person_id: int, db: Session = Depends(get_db), user: UserModel = Depends(get_current_user)) -> Response:

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Você não está autenticado."
        )

    if not delete_person_service(db, person_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Não foi possível deletar o usuário solicitado."
        )

    return Response(
        status_code=HTTPStatus.NO_CONTENT.value
    )
