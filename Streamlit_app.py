import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Titre de l'application
st.set_page_config(page_title="Prédiction de Fleur Iris", layout="wide")

# Menu latéral
st.sidebar.title("Menu de Navigation")
menu = st.sidebar.radio("Choisir une option", ["Accueil", "Prédiction de Fleur", "A propos"])

# Chargement des données Iris
iris = load_iris()
X = iris.data  # Les caractéristiques : longueur et largeur des sépales et des pétales
y = iris.target  # Les labels : type de fleur (Setosa, Versicolor, Virginica)

# Pré-traitement des données (normalisation)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Entraînement du modèle (SVM)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
model = SVC(kernel='linear')  # Support Vector Classifier
model.fit(X_train, y_train)

# Accueil - Page principale
if menu == "Accueil":
    st.title("Bienvenue sur l'application de prédiction de type de fleur Iris")
    st.write("""
        Cette application utilise les dimensions de la fleur Iris pour prédire son type. 
        Les utilisateurs peuvent entrer les dimensions d'une fleur et obtenir la prédiction de son type.
    """)

# A propos - Informations sur l'application
elif menu == "A propos":
    st.title("A propos de cette application")
    st.write("""
        L'iris est un célèbre ensemble de données de machine learning qui contient des mesures de fleurs Iris, 
        notamment la longueur et la largeur des sépales et des pétales. 
        L'objectif de cette application est de prédire le type de fleur Iris (Setosa, Versicolor, Virginica) 
        en fonction de ces mesures.
    """)

# Prédiction de Fleur - Formulaire interactif
elif menu == "Prédiction de Fleur":
    st.title("Prédiction du type de fleur Iris")
    st.write("""
        Entrez les dimensions de la fleur et nous vous dirons quel type de fleur il s'agit.
    """)

    # Formulaire pour entrer les dimensions de la fleur
    sepal_length = st.number_input("Longueur du sépale (cm)", min_value=0.0, max_value=10.0, value=5.0)
    sepal_width = st.number_input("Largeur du sépale (cm)", min_value=0.0, max_value=10.0, value=3.0)
    petal_length = st.number_input("Longueur du pétale (cm)", min_value=0.0, max_value=10.0, value=4.0)
    petal_width = st.number_input("Largeur du pétale (cm)", min_value=0.0, max_value=10.0, value=1.3)

    # Lorsque l'utilisateur clique sur le bouton pour prédire
    if st.button("Prédire le type de fleur"):
        # Préparation de la donnée entrée par l'utilisateur
        input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
        input_data_scaled = scaler.transform(input_data)  # Normalisation des données

        # Prédiction avec le modèle
        prediction = model.predict(input_data_scaled)
        flower_type = iris.target_names[prediction][0]

        # Affichage des résultats
        st.write(f"Le type de la fleur est : {flower_type}")

        # Affichage d'un graphique de la fleur
        fig, ax = plt.subplots()
        ax.scatter(sepal_length, sepal_width, label="Sépale", color="blue", s=100, marker="o")
        ax.scatter(petal_length, petal_width, label="Pétale", color="red", s=100, marker="x")
        ax.set_title("Visualisation des dimensions de la fleur")
        ax.set_xlabel("Longueur (cm)")
        ax.set_ylabel("Largeur (cm)")
        ax.legend()
        st.pyplot(fig)

