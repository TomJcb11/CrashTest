from pages.config import MONGODB_URI
from pymongo import MongoClient

def connect_to_mongodb():
    client = MongoClient(MONGODB_URI)
    db = client.my_database
    return db

def insert_one_document(collection, document):
    result = collection.insert_one(document)
    return result.inserted_id

def insert_many_documents(collection, documents):
    result = collection.insert_many(documents)
    return result.inserted_ids

def main():
    # Utiliser les configurations pour se connecter à MongoDB
    db = connect_to_mongodb()
    print("Connected to MongoDB")
    
    # Exemple d'insertion d'un document dans la colection my_collection
    collection = db.countryAPI
    document = {"name": "John Doe", "age": 30, "email": "john.doe@example.com"}
    
    document_id = insert_one_document(collection, document)
    print(f"Document inserted with id: {document_id}")

    # Exemple d'insertion de plusieurs documents
    documents = [
        {"name": "Jane Doe", "age": 25, "email": "jane.doe@example.com"},
        {"name": "Alice", "age": 28, "email": "alice@example.com"}
    ]
    document_ids = insert_many_documents(collection, documents)
    print(f"Documents inserted with ids: {document_ids}")
    
if __name__ == "__main__":
    main()