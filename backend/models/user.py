from dataclasses import dataclass

from sqlalchemy import Column, Integer, String

from backend.db import Db


# define a model
# the typehints are necessary for serialising
@dataclass
class User(Db.get_base()):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True)
    username: str = Column(String(50), unique=True)

    def __init__(self, username=None):
        self.username = username