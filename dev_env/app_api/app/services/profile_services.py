from typing import List

from fastapi import HTTPException, status

from sqlalchemy.orm import Session

from sqlalchemy.exc import IntegrityError, ProgrammingError, DataError, PendingRollbackError

from app.configurations.database import Base, engine
from app.models.profile_model import ProfileModel
from app.schemas.profile_schema import ProfileSchema, ProfileCreateSchema, ProfileUpdateSchema


def get_profile_by_id_service(db: Session, profile_id: int) -> ProfileSchema:
    """
    this service return one profile with they id
    :param db:
    :param profile_id:
    :return:
    """
    return db.query(ProfileModel).get(profile_id)


def create_profile_service(db: Session, profile_data: ProfileCreateSchema) -> ProfileSchema:
    """
    this service create one new profile in database.
    :param db:
    :param profile_data:
    :return:
    """

    try:
        Base.metadata.create_all(engine)
        new_profile = ProfileModel(**profile_data.dict())
        db.add(new_profile)
        db.commit()
        db.refresh(new_profile)

        return new_profile

    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Não foi possível Criar o Perfil. Verifique se os dados foram preenchidos corretamente."
        )

    except ProgrammingError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Não foi possível Criar o Perfil, verifique se os dados foram preenchidos corretamente."
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


def get_all_profiles_service(db: Session) -> List[ProfileSchema]:
    """
    This Service get all profiles in database
    :param db:
    :return:
    """
    return db.query(ProfileModel).all()


def update_profile_service(db: Session, profile_id: int, update_data: ProfileUpdateSchema) -> ProfileSchema:
    """
    This service update the profile data in database.
    :param db:
    :param profile_id:
    :param update_data:
    :return:
    """

    try:
        if profile := get_profile_by_id_service(db, profile_id):
            update_values = {key: value for key, value in update_data if value}
            db.query(ProfileModel).filter(ProfileModel.id == profile.id).update(update_values)
            db.commit()
            db.refresh(profile)
            return profile

    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Não foi possível Atualizar o Perfil. Verifique se os dados foram preenchidos corretamente."
        )

    except ProgrammingError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Não foi possível Atualizar o Perfil, verifique se os dados foram preenchidos corretamente."
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


def delete_profile_service(db: Session, profile_id: int) -> bool:
    """
    This service remove one profile to database
    :param db:
    :param profile_id:
    :return:
    """
    if profile := get_profile_by_id_service(db, profile_id):
        db.query(ProfileModel).filter(ProfileModel.id == profile.id).delete()
        db.commit()

        return True

    return False
