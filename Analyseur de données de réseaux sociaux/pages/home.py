import streamlit as st

def home():
    st.title("Bienvenue sur le Dashboard")
    st.write("Sélectionnez une option dans la barre de navigation.")
    
    # Liens vers les autres pages
    st.page_link("pages/test2.py", label="Map", icon="🌍")
    st.page_link("pages/country.py", label="Country", icon="🏳️")