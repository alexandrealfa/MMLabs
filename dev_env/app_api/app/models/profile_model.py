from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

from app.configurations.database import Base


class ProfileModel(Base):
    __tablename__ = "profile"
    id: int = Column(Integer, primary_key=True)
    profile_url: str = Column(String)
    banner_profile_url: str = Column(String)
    bio: str = Column(String(2000))
    user_id: int = Column(Integer, ForeignKey("users.id",
                                              onupdate="CASCADE",
                                              ondelete="CASCADE"))

    user = relationship("UserModel",
                        uselist=False,
                        backref=backref("profile",
                                        lazy="joined"),
                        lazy="joined")

