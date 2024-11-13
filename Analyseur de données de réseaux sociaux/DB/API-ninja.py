import requests
from DB.APIkey import MONGODB_URI
from pymongo import MongoClient

europe_countries = [
    'France', 'Germany', 'Spain', 'Italy', 'Portugal', 'Belgium', 'Netherlands', 'Switzerland',
    'Austria', 'Sweden', 'Norway', 'Denmark', 'Finland', 'Ireland', 'Poland', 'Czech Republic',
    'Hungary', 'Greece', 'Turkey', 'Russia', 'United Kingdom'
]

north_africa_countries = [
    'Algeria', 'Egypt', 'Morocco', 'Tunisia', 'Libya'
]

americas_countries = [
    'United States', 'Canada', 'Mexico', 'Cuba', 'Haiti', 'Jamaica', 'Dominican Republic', 'Guatemala'
    ]
asian_countries = [
    'China', 'India', 'Indonesia', 'Pakistan', 'Bangladesh', 'Japan', 'Philippines', 'Vietnam','south korea'
]

# Fonction pour se connecter à MongoDB
def connect_to_mongodb():
    client = MongoClient(MONGODB_URI)
    db = client.my_database
    return db

# Fonction pour insérer un document dans une collection
def insert_one_document(collection, document):
    result = collection.insert_one(document)
    return result.inserted_id

# Fonction principale
def main():
    # Se connecter à MongoDB
    db = connect_to_mongodb()
    print("Connected to MongoDB")
    
    # Collection pour stocker les réponses de l'API
    collection = db.countryAPI
    
    # Faire une requête à l'API pour chaque pays d'Afrique du Nord
    for country in asian_countries:
        api_url = f'https://api.api-ninjas.com/v1/population?country={country}'
        response = requests.get(api_url, headers={'X-Api-Key': 'QZ2s4vD9a9igD/xja3Q1FQ==xgkKqgn6jWfRBpYW'})
        
        if response.status_code == requests.codes.ok:
            data = response.json()
            document = {"country": country,"region":"asia", "data": data}
            document_id = insert_one_document(collection, document)
            print(f"Document for {country} inserted with id: {document_id}")
        else:
            print(f"Error for {country}: {response.status_code}, {response.text}")

if __name__ == "__main__":
    main()