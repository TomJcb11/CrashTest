import streamlit as st 

st.header("Streamlit_ Bescherelle")
tab1, tab2, tab3 = st.tabs(["1 er groupe", "2 ème groupe", "3 ème groupe"])

with tab1:
    st.text_input("Rechercher un verbe", key="input_tab1")
    st.markdown("""
                ### Conjugaison des verbes du 1-er groupe
                Les verbes du premier groupe sont les verbes qui se terminent par e, r. Exemples : 
                - chanter, 
                - regarder, 
                - crier.
                - etc,...
               """)
    
    

with tab2:
    st.markdown("""
                ### Conjugaison des verbes du 2-ème groupe
                Les verbes du deuxième groupe sont les verbes qui se terminent par ir. Exemples : 
                - finir, 
                - choisir""")
    st.text_input("Rechercher un verbe", key="input_tab2")

with tab3:
    st.text_input("Rechercher un verbe", key="input_tab3")
    st.markdown("""
                ### Conjugaison des verbes du 3-ème groupe
                Les verbes du troisième groupe sont tous les autres verbes. Ils sont très nombreux et très variés. Par exemple: 
                 - aller
                 - avoir
                 - être
                 - faire 
                 - dire
                 - pouvoir 
                 - vouloir
                 - savoir
                 - etc...
                 """ )
    
    st.text("ici globalement force pour implémenter ca")
    
    