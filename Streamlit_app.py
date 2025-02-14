import streamlit as st
import pandas as pd
#import seaborn as sns
import altair as alt

#st.title("WELCOME TO WAFFO DASHBORD FOR IRIS WORK 2025")
#st.subheader("Creating dashboard...")
#st.write("hello world")

#df = sns.load_dataset('Iris')
st.set_page_config(page_title="Dashboard avec Menu Latéral", layout="wide")
st.sidebar.title("Menu de Navigation")
menu = st.sidebar.radio("Sélectionner une option", ["Vue d'ensemble", "Statistiques", "Visualisation"])

