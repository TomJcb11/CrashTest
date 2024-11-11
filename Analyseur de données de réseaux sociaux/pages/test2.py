import streamlit as st
import pandas as pd
from pymongo import MongoClient
from config import MONGODB_URI
import plotly.graph_objects as go

# Fonction pour se connecter à MongoDB
def connect_to_mongodb():
    client = MongoClient(MONGODB_URI)
    db = client.my_database
    return db

# Fonction pour récupérer les données de MongoDB et les convertir en DataFrame
def get_all_country_data():
    db = connect_to_mongodb()
    collection = db.countryAPI
    data = list(collection.find({}, {"_id": 0, "data": 1, "country": 1, "region": 1}))
    
    # Extraire les données de population historique et de prévision
    all_data = []
    for document in data:
        country = document['country']
        region = document['region']
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
    return df

# Fonction pour récupérer la liste des propriétés uniques des pays
def get_unique_properties():
    db = connect_to_mongodb()
    collection = db.countryAPI
    data = list(collection.find())
    
    # Extraire les propriétés uniques
    properties = set()
    for document in data:
        if 'data' in document and isinstance(document['data'], dict):
            for entry in document['data'].get('historical_population', []):
                properties.update(entry.keys())
            for entry in document['data'].get('population_forecast', []):
                properties.update(entry.keys())
    
    return list(properties)

st.header("Streamlit-Plotly: Carte du Monde avec Indicateurs")

# Créer des onglets
tab1, tab2 = st.tabs(["World Map", "Countries"])

# Récupérer les données de MongoDB
df = get_all_country_data()
unique_properties = get_unique_properties()

# Contenu de l'onglet 1
with tab1:
    # Sélectionner une année
    years = df['year'].unique()
    selected_year = st.selectbox("Sélectionnez une année", sorted(years))
    
    # Sélectionner un indicateur
    selected_indicator = st.selectbox("Sélectionnez un indicateur", unique_properties)
    
    # Créer un modal pour les options de personnalisation
    @st.dialog("Options de personnalisation")
    def customize_options():
        st.write("Options de personnalisation")
        show_ocean = st.checkbox("Afficher les océans", value=True)
        projection_type = st.radio("Type de projection", ('equirectangular', 'mercator', 'orthographic', 'natural earth', 'kavrayskiy7', 'miller', 'robinson', 'eckert4', 'azimuthal equal area'))
        colorscale = st.selectbox("Échelle de couleurs", ['Yellow-Red', 'Blue-Green', 'Purple-Orange', 'Red-Black'])
        if st.button("Appliquer"):
            st.session_state.custom_options = {"show_ocean": show_ocean, "projection_type": projection_type, "colorscale": colorscale}
            st.session_state.modal_open = False
            st.rerun()

    if "custom_options" not in st.session_state:
        show_ocean = True
        projection_type = 'equirectangular'
        colorscale = 'Yellow-Red'
    else:
        custom_options = st.session_state.custom_options
        show_ocean = custom_options.get("show_ocean", True)
        projection_type = custom_options.get("projection_type", 'equirectangular')
        colorscale = custom_options.get("colorscale", 'Yellow-Red')

    if "modal_open" not in st.session_state:
        st.session_state.modal_open = False

    if st.session_state.modal_open:
        customize_options()

    if st.button("Personnaliser"):
        st.session_state.modal_open = True
        customize_options()
    
    # Définir les échelles de couleurs
    colorscales = {
        'Yellow-Red': [
            [0, 'yellow'], 
            [0.1, 'gold'], 
            [0.2, 'orange'], 
            [0.3, 'darkorange'], 
            [0.4, 'orangered'], 
            [0.5, 'red'], 
            [0.6, 'darkred'], 
            [0.7, 'brown'], 
            [0.8, 'maroon'], 
            [0.9, 'black'], 
            [1, 'purple']
        ],
        'Blue-Green': [
            [0, 'blue'], 
            [0.1, 'lightblue'], 
            [0.2, 'cyan'], 
            [0.3, 'aquamarine'], 
            [0.4, 'lightgreen'], 
            [0.5, 'green'], 
            [0.6, 'darkgreen'], 
            [0.7, 'forestgreen'], 
            [0.8, 'seagreen'], 
            [0.9, 'teal'], 
            [1, 'darkcyan']
        ],
        'Purple-Orange': [
            [0, 'purple'], 
            [0.1, 'violet'], 
            [0.2, 'magenta'], 
            [0.3, 'orchid'], 
            [0.4, 'plum'], 
            [0.5, 'pink'], 
            [0.6, 'lightpink'], 
            [0.7, 'peachpuff'], 
            [0.8, 'coral'], 
            [0.9, 'orange'], 
            [1, 'darkorange']
        ],
        'Red-Black': [
            [0, 'red'], 
            [0.1, 'darkred'], 
            [0.2, 'brown'], 
            [0.3, 'maroon'], 
            [0.4, 'black'], 
            [0.5, 'darkgray'], 
            [0.6, 'gray'], 
            [0.7, 'lightgray'], 
            [0.8, 'silver'], 
            [0.9, 'gainsboro'], 
            [1, 'white']
        ]
    }
    
    # Filtrer les données pour l'année sélectionnée
    df_filtered = df[df['year'] == selected_year]
    
    # Remplacer les valeurs manquantes par 0
    df_pivot = df_filtered.pivot_table(index='country', values=selected_indicator, fill_value=0).reset_index()
    
    # Fonction pour créer une carte avec des pays colorés selon un indicateur
    def create_colored_world_map(df, selected_indicator, selected_year, show_ocean, projection_type, colorscale):
        # Extraire les noms des pays et les valeurs des indicateurs
        countries = df['country'].tolist()
        values = df[selected_indicator].tolist()

        # Créer des liens HTML pour chaque pays
        links = [f'<a href="/?country={country}" target="_self">{country}</a>' for country in countries]

        # Créer une carte choroplèthe avec des pays colorés selon l'indicateur
        fig = go.Figure(go.Choropleth(
            locationmode='country names',
            locations=countries,  # Liste des pays
            z=values,  # Valeurs de l'indicateur pour colorer les pays
            text=links,  # Liens HTML pour les étiquettes de survol
            colorscale=colorscales[colorscale],  # Échelle de couleurs sélectionnée
            showscale=True,  # Afficher la barre de couleurs
            marker_line_color='black',  # Couleur des lignes de contour des pays
            marker_line_width=0.5,  # Largeur des lignes de contour des pays
            hovertemplate='%{text}  %{z}<extra></extra>'  # Personnaliser les étiquettes de survol
        ))

        # Mettre à jour les propriétés de la carte
        fig.update_geos(
            visible=True,
            resolution=110,
            showcountries=True,
            countrycolor="Black",
            showcoastlines=False,
            showland=True,
            landcolor="white",
            showocean=show_ocean,
            oceancolor="LightBlue" if show_ocean else "white",
            projection_type=projection_type
        )

        fig.update_layout(
            title_text='{} par Pays en {}'.format(selected_indicator, selected_year),
            geo=dict(
                showframe=False,
                showcoastlines=True,
                projection_type=projection_type
            ),
            autosize=True,
            height=400
        )

        return fig

    # Créer la carte colorée
    fig = create_colored_world_map(df_pivot, selected_indicator, selected_year, show_ocean, projection_type, colorscale)

    # Styliser le DataFrame avec CSS
    st.markdown(
        """
        <style>
        .dataframe-container {
            width: 100%;
            height: 400px;
            overflow: auto;
        }
        .dataframe-container table {
            width: 100%;
            border-collapse: collapse;
        }
        .dataframe-container th {
            background-color: #FF0000;
            color: white;
        }
        .dataframe-container td, .dataframe-container th {
            border: 1px solid #ddd;
            padding: 8px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Intégrer la carte à une page Streamlit
    st.plotly_chart(fig, use_container_width=True)

    # Afficher le DataFrame avec st.dataframe
    st.dataframe(df_pivot)

# Contenu de l'onglet 2
with tab2:
    st.title("Liste des Pays")
    selected_countries = st.multiselect("Sélectionnez un ou plusieurs pays", df['country'].unique())
    if selected_countries:
        st.experimental_set_query_params(page="country", country=selected_countries[0])
        st.experimental_rerun()