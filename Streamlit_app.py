import streamlit as st
import pandas as pd
import numpy as np
#import seaborn as sns
import altair as alt

#st.title("WELCOME TO WAFFO DASHBORD FOR IRIS WORK 2025")
#st.subheader("Creating dashboard...")
#st.write("hello world")

#df = sns.load_dataset('Iris')
st.set_page_config(page_title="Dashboard avec Menu Latéral", layout="wide")
st.sidebar.title("Menu de Navigation")
menu = st.sidebar.radio("Sélectionner une option", ["Vue d'ensemble", "Statistiques", "Visualisation"])

np.random.seed(42)
data = pd.DataFrame({
    'Colonne A': np.random.randn(100),
    'Colonne B': np.random.randn(100),
    'Colonne C': np.random.rand(100)
})

if menu == "Vue d'ensemble":
    st.title("Vue d'ensemble des données")
    st.write("""
        Ce tableau montre un aperçu des données générées aléatoirement pour le dashboard.
    """)
    st.dataframe(data.head())

elif menu == "Statistiques":
    st.title("Statistiques descriptives")

elif menu == "Visualisation":
    st.title("Visualisation des données")
    st.write("""
        Ici, vous pouvez visualiser les données sous forme de graphiques.
    """)
    st.write("""
        Ces statistiques donnent un aperçu de la distribution des valeurs dans le jeu de données.
    """)
    st.write(data.describe())
