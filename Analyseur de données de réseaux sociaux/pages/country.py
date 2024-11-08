import streamlit as st

def country_view(countryName):
    if countryName:
        st.header(f"Page dédiée pour {countryName}")
        st.write(f"Affichage des indicateurs pour {countryName}...")
        # Ajoutez ici des graphiques et des indicateurs spécifiques pour le pays
        # Exemple : st.bar_chart(data)
    else:
        st.write("Sélectionnez un pays dans le tableau.")

if __name__ == "__main__":
    country = st.experimental_get_query_params().get("country", [None])[0]
    country_view(country)