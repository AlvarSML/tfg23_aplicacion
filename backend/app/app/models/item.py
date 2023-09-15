from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base

from .user import User  # noqa: F401


class Item(Base):
    __tablename__="item"

    id: int = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    #owner_id = Column(Integer, ForeignKey("user.id"))

    owner_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    #owner: Mapped["User"] = relationship(back_populates="items")
    owner: Mapped["User"] = relationship(back_populates="items")
