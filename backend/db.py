import importlib
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


class __Db:
    def __init__(self, file_path: str = 'sqlite:///database.db', model_path: str = 'models'):
        self.__file_path = file_path
        self.__base = declarative_base()
        self.__model_path = model_path
        self.__engine = None
        self.__session = None

    def __import_models(self):
        location = os.path.dirname(os.path.realpath('main')) + os.sep + self.__model_path
        for file in os.listdir(location):
            if file[-3:] == ".py":
                importlib.import_module(self.__model_path.replace('/', '.') + '.' + file[:-3])

    def start(self):
        self.__engine = create_engine(self.__file_path)
        self.__session = scoped_session(
            sessionmaker(autocommit=False, autoflush=False, bind=self.__engine)
        )
        self.__base.query = self.__session.query_property()

        self.__import_models()
        self.__base.metadata.create_all(bind=self.__engine)

    def get_base(self):
        return self.__base

    def get_session(self):
        return self.__session

    def set_model_path(self, path: str):
        self.__model_path = path

    def set_file_path(self, path: str):
        self.__file_path = path

Db = __Db()