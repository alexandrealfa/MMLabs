from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session
from app.services.db_services import get_db
from app.services.person_services import get_person_service

from app.schemas.person_schema import PersonSchema


router_person = APIRouter()


@router_person.get("/person/{current_id}", response_model=PersonSchema)
def get_current_person(current_id: int, db: Session = Depends(get_db)) -> PersonSchema:
    """
    This router return data by one person, with they id.
    :param current_id:
    :param db:
    :return:
    """

    if person := get_person_service(db, current_id):
        return person

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="O Id informado não está registrado em nosso banco de dados."
    )

