import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Charger le fichier CSV du jeu de données Iris
#@st.cache
def load_data():
    # Charger le fichier CSV localement
    df=pd.read_csv('Iris.csv', delimiter=";")
    return df
df = load_data()

# Afficher le jeu de données
#st.title("Prédiction du type de fleur Iris")
#st.write("Voici un aperçu du jeu de données Iris :")
#st.dataframe(df.head())  # Affiche les 5 premières lignes du dataset

# Préparation des données pour l'entraînement
X = df.drop(columns=["Species"])  # Variables explicatives
y = df["Species"]  # Variable cible

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Entraînement du modèle Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Prédiction sur l'ensemble de test pour évaluer le modèle
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Affichage de la précision du modèle
#st.write(f"Précision du modèle : {accuracy:.2f}")

# Sauvegarder le modèle pour une utilisation ultérieure
with open('iris_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

# Interface pour saisir les dimensions de la fleur
st.sidebar.title("Prédiction")
menu = st.sidebar.radio("Sélectionner une option", ["ACCEUIL", "PREDICTION", "A PROPOS DE NOUS"])
if menu == "ACCEUIL":
    st.title("ACCEUIL")
    st.write("Bienvenue sur notre API de prédiction des especes de fleurs entrainée avec le jeu de donées <<Iris_Dataset.csv>>")
    st.write("")
    st.write("Voici un aperçu du jeu de données Iris (les 05 premières lignes) :")
    st.dataframe(df.head()) 
    st.write("")
    st.write("Rendez-vous au menu préddiction, entrer les dimension que vous voulez, et notre plateforme se chargera de vous prédire de quelle espèces cette fleurs appatiens.")
    
# Formulaire pour saisir les dimensions
elif menu == "PREDICTION":
    st.title("PREDICTION DES FLEURS")
    # Affichage de la précision du modèle
    st.write(f"Précision du modèle : {accuracy:.2f}")
    st.write("Entrez les dimensions de la fleur :")
    sepal_length = st.number_input("Longueur du sépale (cm)", min_value=0.0, max_value=10.0, value=5.0)
    sepal_width = st.number_input("Largeur du sépale (cm)", min_value=0.0, max_value=10.0, value=3.0)
    petal_length = st.number_input("Longueur du pétale (cm)", min_value=0.0, max_value=10.0, value=4.0)
    petal_width = st.number_input("Largeur du pétale (cm)", min_value=0.0, max_value=10.0, value=1.3)

# Prédiction du type de fleur
    if st.button("Prédire"):
        # Créer un DataFrame à partir des entrées de l'utilisateur
        user_input = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]], 
                              columns=["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"])
elif menu == "A PROPOS DE NOUS"
    st.write("Etudiant à l'ENS de Yaoundé, filière informatique")
    st.write("@Waffo")

    # Prédire le type de fleur
        predicted_species = model.predict(user_input)
        st.write(f"La fleur prédit est de type : {predicted_species[0]}")
