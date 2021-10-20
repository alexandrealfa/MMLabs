from typing import List

from fastapi import HTTPException, status

from sqlalchemy.orm import Session

from sqlalchemy.exc import IntegrityError, ProgrammingError, DataError, PendingRollbackError

from app.configurations.database import Base, engine
from app.models.person_model import PersonModel
from app.schemas.person_schema import PersonSchema, PersonCreateSchema, PersonUpdateSchema


def create_new_person_service(db: Session, new_person: PersonCreateSchema) -> PersonSchema:
    """
    This service register one new patient in this route.
    :param db:
    :param new_person:
    :return:
    """

    try:
        Base.metadata.create_all(engine)
        db_new_person = PersonModel(**new_person.dict())
        db.add(db_new_person)
        db.commit()
        db.refresh(db_new_person)

        return db_new_person

    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Não foi possível Criar o Perfil. Verifique se os dados foram preenchidos corretamente."
        )

    except ProgrammingError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Não foi possível Criar o Perfil. Verifique se os dados foram preenchidos corretamente."
        )

    except PendingRollbackError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cpf já está registrado!."
        )

    except DataError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Os Dados estão preenchidos de forma incorreta."
        )


def get_person_service(db: Session, person_id: int) -> PersonSchema:
    """
    This service return one person at database with id param set
    :param db:
    :param person_id:
    :return:
    """
    return db.query(PersonModel).get(person_id)


def get_all_person_service(db: Session) -> List[PersonSchema]:
    """
    This Service return all persons in database.
    :param db:
    :return:
    """
    return db.query(PersonModel).all()


def update_person_service(db: Session, person_id: int, data_update: PersonUpdateSchema) -> PersonSchema:
    """
    This service update the person data in database.
    :param db:
    :param person_id:
    :param data_update:
    :return:
    """

    try:
        if person := get_person_service(db, person_id):
            update_values = {
                key: value for key, value in data_update if value
            }
            db.query(PersonModel)\
                .filter(PersonModel.id == person_id)\
                .update(update_values)
            db.commit()
            db.refresh(person)

            return person

    except IntegrityError:
        pass

    except ProgrammingError:
        pass

    except PendingRollbackError:
        pass

    except DataError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Os Dados estão preenchidos de forma incorreta."
        )


def delete_person_service(db: Session, person_id: int):
    """
    This service delete one person in database
    :param db:
    :param person_id:
    :return:
    """

    if person := get_person_service(db, person_id):
        db.query(PersonModel).filter(PersonModel.id == person.id).delete()
        db.commit()

        return True

    return False
