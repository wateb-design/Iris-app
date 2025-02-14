import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

#st.title("WELCOME TO WAFFO DASHBORD FOR IRIS WORK 2025")
#st.subheader("Creating dashboard...")
#st.write("hello world")

st.set_page_config(
    page_title="US WAFFO DASHBORD FOR IRIS APP",
    #page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")
