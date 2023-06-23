from datetime import datetime, timedelta
from typing import Literal

from models.configs.mongodb_configs import MongoConfig as Config
from pymongo.database import Database
from pymongo.errors import WriteError


class CollectionHandler:
    def __init__(self, collection_name: str, db_connection: Database) -> None:
        self.collection_name = collection_name
        self.__db_connection = db_connection
        self.__collection = self.__db_connection.get_collection(collection_name)
        self.config = Config()

    def insert_document(self, document: dict) -> None:
        # collection = self.__db_connection.get_collection(self.__collection)
        try:
            self.__collection.insert_one(document)
            print(f"Document {document} inserted successfully")
        except WriteError as eror:
            print(f"[ERROR] Insert document failed - {eror}")

    def insert_list_of_documents(self, documents: list[dict]) -> None:
        # collection = self.__db_connection.get_collection(self.__collection)
        try:
            self.__collection.insert_many(documents)
            print(f"List {documents} inserted successfully")
        except WriteError as error:
            print(f"[ERROR] Insert list of documents failed - {error}")

    def select_many(
        self,
        query: dict = None,
        exclude_id: bool = True,
        sort_by: tuple[str, int] = None,
    ) -> list[dict]:
        if query is None:
            query = {}

        if exclude_id:
            opt = {"_id": 0}

        # collection = self.__db_connection.get_collection(self.__collection)

        data = self.__collection.find(query, opt)

        if sort_by is not None:
            data = data.sort([sort_by])

        return [*data]

    def select_one(self, query: dict = None, exclude_id: bool = True) -> dict:
        if query is None:
            query = {}

        if exclude_id:
            opt = {"_id": 0}

        # collection = self.__db_connection.get_collection(self.__collection)
        return self.__collection.find_one(query, opt)

    def edit_one(
        self,
        query: dict,
        edit: dict,
        mode: str = "set",
    ) -> None:
        mode = self.config.EDIT_OPERATORS[mode]
        response = self.__collection.update_one(query, {mode: edit})
        print(f"Edited records: {response.modified_count}")

    def edit_many(
        self,
        query: dict,
        edit: dict,
        mode: str = "set",
    ) -> None:
        mode = self.config.EDIT_OPERATORS[mode]
        response = self.__collection.update_many(query, {mode: edit})
        print(f"Edited records: {response.modified_count}")

    def delete_one(self, query: dict) -> None:
        response = self.__collection.delete_one(query)
        print(f"Deleted records: {response.deleted_count}")

    def delete_many(self, query: dict) -> None:
        response = self.__collection.delete_many(query)
        print(f"Deleted records: {response.deleted_count}")

    def create_index(
        self, index_name: str, order: Literal[-1, 1] = 1, ttl: int = None
    ) -> None:
        if ttl is not None:
            ttl = timedelta(seconds=ttl)
            self.__collection.create_index(index_name, expireAfterSeconds=ttl.seconds)
        else:
            self.__collection.create_index(index_name, order)
