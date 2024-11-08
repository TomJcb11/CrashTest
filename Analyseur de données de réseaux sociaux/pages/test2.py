import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from itertools import cycle

# Créer des onglets
tab1, tab2 = st.tabs(["World Map", "Countries"])

country_values = [
            ('France', 65), ('Germany', 70), ('Spain', 75), ('Italy', 80), ('Portugal', 85),
            ('Japan', 90), ('United States', 95), ('Canada', 100), ('Brazil', 105), ('Argentina', 110),
            ('Australia', 115), ('India', 120), ('China', 125), ('South Africa', 130), ('Russia', 135),
            ('United Kingdom', 140),('Belgium',80),('Algeria',200)
        ]
# Contenu de l'onglet 1
with tab1:
    # Fonction pour créer une carte avec des pays colorés selon un indicateur
    def create_colored_world_map(country_values):

        
        # Extraire les noms des pays et les valeurs des indicateurs
        countries = [country for country, value in country_values]
        values = [value for country, value in country_values]

        # Créer des liens HTML pour chaque pays

        # Créer une carte choroplèthe avec des pays colorés selon l'indicateur
        fig = go.Figure(go.Choropleth(
            locationmode='country names',
            locations=countries,  # Liste des pays
            z=values,  # Valeurs de l'indicateur pour colorer les pays
            text=countries,  # Liens HTML pour les étiquettes de survol,  # Liens HTML pour les étiquettes de survol
            colorscale=[[0, 'blue'], [0.5, 'yellow'], [1, 'red']],  # Échelle de couleurs pour trois niveaux
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
            showocean=False,
            projection_type='equirectangular'
        )

        fig.update_layout(
            title_text='Carte des pays avec indicateurs',
            geo=dict(
                showframe=False,
                showcoastlines=True,
                projection_type='equirectangular'
            ),
            autosize=True,
            height=400
        )

        return fig

    # Créer la carte colorée
    fig = create_colored_world_map(country_values)


    df = pd.DataFrame(country_values, columns=['Country', 'Value'])

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
    st.title("Carte du Monde avec Indicateurs")
    st.plotly_chart(fig, use_container_width=True)

    # Récupérer le paramètre d'URL pour le pays
    country = st.experimental_get_query_params().get("country", [None])[0]
    st.markdown('<div class="dataframe-container">' + df.to_html(index=False) + '</div>', unsafe_allow_html=True)
# Contenu de l'onglet 2
with tab2:
    st.title("Liste des Pays")
    selected_country = st.multiselect("Choose a country", [country for country, value in country_values])
    
            
            