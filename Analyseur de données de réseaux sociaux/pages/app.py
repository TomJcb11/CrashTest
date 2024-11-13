import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import time

#import des différentes fonctions 
from DB.queries import get_all_country_data, get_unique_properties
from functions.data_processing import process_country_data
from functions.visualization import create_colored_world_map
from pages.styles.colorscales import colorscales
from pages.styles.custom_css import load_custom_css

st.header("Streamlit-Plotly: Carte du Monde avec Indicateurs")

# Charger le CSS personnalisé
st.markdown(load_custom_css(), unsafe_allow_html=True)

# Créer des onglets
tab1, tab2 = st.tabs(["World Map", "Countries"])

# Récupérer les données de MongoDB
data = get_all_country_data()
df = process_country_data(data)
unique_properties = get_unique_properties()

# Contenu de l'onglet 1
with tab1:
    # Sélectionner un indicateur
    selected_indicator = st.selectbox("Sélectionnez un indicateur", unique_properties)
    
    # Activer le mode "time lapse"
    time_lapse = st.toggle("Activer le mode Time Lapse")
    
    if time_lapse:
        years = sorted(df['year'].unique())
        start_year, end_year = st.select_slider("Sélectionnez la période", options=years, value=(years[0], years[-1]))
        timelapse = [start_year, end_year]
    else:
        years = df['year'].unique()
        selected_year = st.select_slider("Sélectionnez une année", options=sorted(years), value=(years[0]))
        timelapse = selected_year
    
    # Créer un modal pour les options de personnalisation
    @st.dialog("Options de personnalisation")
    def customize_options():
        st.write("Options de personnalisation")
        show_ocean = st.toggle("Afficher les océans", value=True)
        projection_type = st.radio("Type de projection", ('equirectangular', 'mercator', 'orthographic', 'natural earth', 'kavrayskiy7', 'miller', 'robinson', 'eckert4', 'azimuthal equal area'))
        colorscale = st.selectbox("Échelle de couleurs", list(colorscales.keys()))
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
    
      # Fonction pour jouer l'animation
    def play_animation(start_year, end_year, available_years):
        animation_container = st.empty()
        for year in available_years:
            try:
                fig = create_colored_world_map(df, selected_indicator, year, show_ocean, projection_type, colorscales[colorscale])
                animation_container.plotly_chart(fig, use_container_width=True)
                time.sleep(0.5)  # Pause de 0.5 secondes entre chaque année
            except KeyError as e:
                st.error(f"Erreur: {e}")

    # Gérer le mode "time lapse"
    if isinstance(timelapse, list):
        start_year, end_year = timelapse
        # Filtrer les années disponibles dans la plage sélectionnée
        available_years = [year for year in years if start_year <= year <= end_year]
        
        # Afficher la carte pour l'année de début
        fig_start = create_colored_world_map(df, selected_indicator, start_year, show_ocean, projection_type, colorscales[colorscale])
        st.plotly_chart(fig_start, use_container_width=True, key=f"start_{start_year}")
        
        # Afficher la carte pour l'année de fin
        fig_end = create_colored_world_map(df, selected_indicator, end_year, show_ocean, projection_type, colorscales[colorscale])
        st.plotly_chart(fig_end, use_container_width=True, key=f"end_{end_year}")
        
        # Bouton pour jouer l'animation
        if st.button("Jouer l'animation"):
            play_animation(start_year, end_year, available_years)
    else:
        try:
            fig = create_colored_world_map(df, selected_indicator, timelapse, show_ocean, projection_type, colorscales[colorscale])
            st.plotly_chart(fig, use_container_width=True, key=f"single_{timelapse}")
            # Filtrer le DataFrame pour afficher uniquement les données de l'année sélectionnée
            df_filtered = df[df['year'] == timelapse][['year', 'country', selected_indicator]]
            st.dataframe(df_filtered)
        except KeyError as e:
            st.error(f"Erreur: {e}")

# Contenu de l'onglet 2
with tab2:
    st.title("Liste des Pays")
    selected_countries = st.multiselect("Sélectionnez un ou plusieurs pays", df['country'].unique())
    