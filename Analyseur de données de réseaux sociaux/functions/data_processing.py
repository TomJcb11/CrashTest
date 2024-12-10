import pandas as pd

def process_country_data(data):
    all_data = []
    for document in data:
            country = document.get('country', 'Unknown')
            region = document.get('region', 'Unknown')
            if 'data' in document and isinstance(document['data'], dict):
                historical_population = document['data'].get('historical_population', [])
                population_forecast = document['data'].get('population_forecast', [])
                
                for entry in historical_population:
                    entry['country'] = country
                    entry['region'] = region
                    entry['type'] = 'historical'
                    all_data.append(entry)
                
                for entry in population_forecast:
                    entry['country'] = country
                    entry['region'] = region
                    entry['type'] = 'forecast'
                    all_data.append(entry)
    
    df = pd.DataFrame(all_data)
    # Convertir les colonnes numériques en type float
    for col in df.columns:
        if col not in ['country', 'region', 'type', 'year']:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    
    return df