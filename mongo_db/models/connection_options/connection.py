# from .mongodb_configs import MongoConfig as Config
from models.configs.mongodb_configs import MongoConfig as Config
from pymongo import MongoClient
from pymongo.database import Database


class MongoConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = self._create_connection_string()
        self.__db_name = Config.DB_NAME
        self.__client = self._create_mongo_client()
        self.__db_connection = None

    def _create_connection_string(self) -> str:
        return f"mongodb://{Config.USERNAME}:{Config.PASSWORD}@{Config.HOST}:{Config.PORT}/?authSource=admin"

    def _create_mongo_client(self) -> MongoClient:
        return MongoClient(self.__connection_string)

    def connect_to_db(self) -> None:
        self.__db_connection = self.__client[self.__db_name]

    def get_db_connection(self) -> Database:
        return self.__db_connection
