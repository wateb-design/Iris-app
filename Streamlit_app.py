pip install seaborn
import streamlit as st
import pandas as pd
import seaborn as sns
import altair as alt

#st.title("WELCOME TO WAFFO DASHBORD FOR IRIS WORK 2025")
#st.subheader("Creating dashboard...")
#st.write("hello world")

df = sns.load_dataset('Iris')
st.subheader('Aperçu des données')
st.dataframe(df.head())
