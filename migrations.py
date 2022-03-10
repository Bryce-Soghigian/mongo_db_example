def db_insert(collection_name:str, obj: dict, DB_NAME: str, client):
    db = client[DB_NAME]
    collection = db[collection_name]
    collection.insert_one(obj)
    print(f'Inserting {obj} into {collection_name}')

def get_all_collection(collection, DB_NAME, client):
    db = client[DB_NAME]
    curr_collection = db[collection]

    return curr_collection.find()

