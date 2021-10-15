from sqlalchemy import Column, Integer, String, ForeignKey

from app.configurations.database import Base


class CommentModel(Base):
    id: int = Column(Integer, primary_key=True)
    comment: str = Column(String)
    user_receiver_id: str = Column(Integer)

    autor_comment_id: int = Column(Integer, ForeignKey("users.id",
                                                       onupdate="CASCADE",
                                                       ondelete="CASCADE"))
