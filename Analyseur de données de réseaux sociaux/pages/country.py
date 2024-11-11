import streamlit as st
from pymongo import MongoClient
from pages.config import MONGODB_URI
import pandas as pd

# Fonction pour se connecter à MongoDB
def connect_to_mongodb():
    client = MongoClient(MONGODB_URI)
    db = client.my_database
    return db

# Fonction pour récupérer les données de MongoDB et les convertir en DataFrame
def get_country_data(country):
    db = connect_to_mongodb()
    collection = db.countryAPI
    data = list(collection.find({"country": country}))
    
    # Extraire les données de population historique et de prévision
    historical_population = data[0]['data']['historical_population']
    population_forecast = data[0]['data']['population_forecast']
    
    # Convertir les données en DataFrame
    df_historical = pd.DataFrame(historical_population)
    df_forecast = pd.DataFrame(population_forecast)
    
    return df_historical, df_forecast

def country_view(countryName):
    if countryName:
        df_historical, df_forecast = get_country_data(countryName)
        st.header(f"Page dédiée pour {countryName}")
        st.write(f"Affichage des indicateurs pour {countryName}...")
        
        st.subheader("Population Historique")
        st.dataframe(df_historical)
        
        st.subheader("Prévisions de Population")
        st.dataframe(df_forecast)
        
        # Ajoutez ici des graphiques et des indicateurs spécifiques pour le pays
        # Exemple : st.line_chart(df_historical[['year', 'population']].set_index('year'))
    else:
        st.write("Sélectionnez un pays dans le tableau.")

if __name__ == "__main__":
    country = st.experimental_get_query_params().get("country", [None])[0]
    country_view(country)