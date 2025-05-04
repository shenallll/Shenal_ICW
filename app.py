# Sri Lanka Conflict Data Dashboard - Streamlit App 

import streamlit as st
import pandas as pd
import plotly.express as px


# Page Configuration

st.set_page_config(page_title="Sri Lanka Conflict Dashboard", layout="wide")
st.title("Sri Lanka Conflict Data Dashboard")
st.write("Explore conflict events, regions, and their impacts across Sri Lanka through this interactive dashboard. Use the filters to narrow down your view and discover insights.")

# Load Preprocessed Data

data = pd.read_csv("preprocessed_conflict_data.csv")


