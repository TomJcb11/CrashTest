from .connect_to_mongodb import connect_to_mongodb
import pandas as pd

def get_all_country_data():
    db = connect_to_mongodb()
    collection = db.countryAPI
    data = list(collection.find({}, {"_id": 0, "data": 1, "country": 1, "region": 1}))
    
    return data

def get_unique_properties():
    db = connect_to_mongodb()
    collection = db.countryAPI
    data = list(collection.find())
    
    properties = set()
    for document in data:
        if 'data' in document and isinstance(document['data'], dict):
            for entry in document['data'].get('historical_population', []):
                properties.update(entry.keys())
            for entry in document['data'].get('population_forecast', []):
                properties.update(entry.keys())
    properties.discard('year')

    return list(properties)