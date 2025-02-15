# app.py

import streamlit as st
import pandas as pd

# Chargement des données Iris (simulées)
# Pour simplifier, nous allons travailler avec une petite table simulée pour la prédiction
data = {
    'species': ['Setosa', 'Versicolor', 'Virginica'],
    'sepal_length_min': [4.3, 4.9, 5.5],
    'sepal_length_max': [5.8, 7.0, 7.9],
    'sepal_width_min': [2.3, 2.2, 2.3],
    'sepal_width_max': [4.4, 3.4, 3.8],
    'petal_length_min': [1.0, 3.0, 4.5],
    'petal_length_max': [1.9, 5.1, 6.9],
    'petal_width_min': [0.1, 1.0, 1.4],
    'petal_width_max': [0.6, 2.0, 2.5]
}

df = pd.DataFrame(data)

# Titre de l'application
st.set_page_config(page_title="Prédiction de Fleur Iris", layout="wide")
st.title("Prédiction du type de fleur Iris")

# Menu latéral
st.sidebar.title("Menu")
menu = st.sidebar.radio("Choisir une option", ["Accueil", "Prédiction de Fleur", "A propos"])

# Accueil
if menu == "Accueil":
    st.write("""
        Bienvenue dans l'application de prédiction du type de fleur Iris.
        Cette application utilise les dimensions des sépales et des pétales pour prédire le type de fleur (Setosa, Versicolor, Virginica).
    """)

# A propos
elif menu == "A propos":
    st.write("""
        L'iris est un célèbre ensemble de données de machine learning qui contient des mesures de fleurs Iris, 
        notamment la longueur et la largeur des sépales et des pétales. 
        Cette application prédit le type de fleur Iris en fonction de ces mesures.
    """)

# Prédiction de Fleur
elif menu == "Prédiction de Fleur":
    st.write("""
        Entrez les dimensions de la fleur Iris ci-dessous pour prédire son type.
    """)

    # Formulaire pour entrer les dimensions de la fleur
    sepal_length = st.number_input("Longueur du sépale (cm)", min_value=0.0, max_value=10.0, value=5.0)
    sepal_width = st.number_input("Largeur du sépale (cm)", min_value=0.0, max_value=10.0, value=3.0)
    petal_length = st.number_input("Longueur du pétale (cm)", min_value=0.0, max_value=10.0, value=4.0)
    petal_width = st.number_input("Largeur du pétale (cm)", min_value=0.0, max_value=10.0, value=1.3)

    # Lorsque l'utilisateur clique sur le bouton pour prédire
    if st.button("Prédire le type de fleur"):
        # Logique de prédiction simple basée sur les dimensions saisies
        predicted_species = "Indéterminé"  # Valeur par défaut

        for index, row in df.iterrows():
            if (sepal_length >= row['sepal_length_min'] and sepal_length <= row['sepal_length_max'] and
                sepal_width >= row['sepal_width_min'] and sepal_width <= row['sepal_width_max'] and
                petal_length >= row['petal_length_min'] and petal_length <= row['petal_length_max'] and
                petal_width >= row['petal_width_min'] and petal_width <= row['petal_width_max']):
                predicted_species = row['species']
                break
        
        # Affichage du résultat
        st.write(f"Le type de la fleur est : {predicted_species}")

