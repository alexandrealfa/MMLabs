from app.configurations.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import backref, relationship
from passlib.hash import bcrypt


class UserModel(Base):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True)
    username: str = Column(String(20), unique=True)
    email: str = Column(String, unique=True)
    password_hash: str = Column(String)
    user_group: str = Column(String(15))
    person_id: int = Column(Integer, ForeignKey("persons.id",
                                                ondelete="CASCADE",
                                                onupdate="CASCADE"),
                            nullable=True,
                            unique=True)

    person: list = relationship('PersonModel',
                                uselist=False,
                                backref=backref("user",
                                                lazy="joined"),
                                lazy="joined")

    comment_list: list = relationship('CommentModel',
                                      backref=backref("user_comment",
                                                      lazy="joined"),
                                      lazy="joined")

    def verify_password(self, password):
        return bcrypt.verify(password, self.password_hash)

    def is_superuser(self):
        if self.user_group.lower() == "admin":
            return True
        return False

    def is_professional(self):
        if self.user_group.lower() == "professional":
            return True
        return False
