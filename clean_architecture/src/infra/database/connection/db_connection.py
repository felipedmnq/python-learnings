from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .db_configs import DBConfig


class DBConnectionHandler:
    def __init__(self) -> None:
        self.configs = DBConfig()
        self.__connection_string = self.configs.CONN_STRING
        self.__engine = self.__create_engine()
        self.session = None

    def __create_engine(self):
        return create_engine(self.__connection_string)

    def get_engine(self):
        sesion = sessionmaker(bind=self.__engine)
        self.session = sesion()
        return self.__engine

    def __enter__(self):
        self.session = sessionmaker(bind=self.__engine)()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.session.close()
