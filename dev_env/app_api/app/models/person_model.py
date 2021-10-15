from sqlalchemy import Column, Integer, String

from app.configurations.database import Base


class PersonModel(Base):
    __tablename__ = 'persons'
    id: int = Column(Integer, primary_key=True)
    cpf: str = Column(String(14), unique=True)
    name: str = Column(String(70))
    phone: str = Column(String)
    birth_date: str = Column(String(10))
