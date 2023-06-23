from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.cursor import CursorType

connection_string = "mongodb://felipedmnq:felipedmnq@localhost:27017/?authSource=admin"
client = MongoClient(connection_string)
df_connection = client["test_db"]

print(type(df_connection))


def create_mongo_collection(records: dict[str, str], collection_name: str) -> None:
    collection = df_connection[collection_name]
    collection.insert_many(records)


def get_collection(collection_name: str) -> Collection:
    return df_connection.get_collection(collection_name)


def find_data(collection_name: str, query: dict) -> CursorType:
    collection = get_collection(collection_name)
    return collection.find(query)


def insert_record_to_collection(collection_name: str, record: dict) -> None:
    collection = get_collection(collection_name)
    collection.insert_one(record)


# test_collection = [{"name": "test", "position": "test"}]
# create_mongo_collection(test_collection, "test_2")

# query = {"name": "test"}

record = {"name": "record_test", "position": [1, 2, 3, 4, 5]}

insert_record_to_collection("test_2", record)

print([*find_data("test_2", {"name": "record_test"})])
