from datetime import datetime, timedelta

from models.configs.mongodb_configs import MongoConfig as Config
from models.connection_options.connection import MongoConnectionHandler

# from models.connection_options.mongodb_configs import MongoConfig as Config
from models.repository.collection_handler import CollectionHandler

db_handler = MongoConnectionHandler()
db_handler.connect_to_db()
db_connection = db_handler.get_db_connection()

test_repo = CollectionHandler(Config.DB_NAME, db_connection)

# query = {"name": "Felipe Vasconcelos"}
# opt = {"_id": 0}
# query = {filter, return_options}
# query = {"cpf": {"$exists": True}}
# query = {"$or": [{"name": "Felipe"}, {"cpf": {"$exists": True}}]}
# sort_by = ("order.pizza", -1)
# edit = {"age": 10}

doc = {
    "name": "Arnold",
    "age": 10,
    "ttl_index": datetime.utcnow() + timedelta(hours=2),
}

# test_repo.insert_document(doc)

# test_repo.edit_registry(query, edit)
# test_repo.edit_many(query, edit, mode="inc")
# test_repo.create_index("ttl_index", ttl=10)
data = test_repo.select_many()
print(data)
