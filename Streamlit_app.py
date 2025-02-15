import streamlit as st
st.set_page_config(page_title="Prédiction de Fleur Iris", layout="wide")

st.sidebar.title("Menu de Navigation")
menu = st.sidebar.radio("Choisir une option", ["Accueil", "Prédiction de Fleur", "A propos"])
