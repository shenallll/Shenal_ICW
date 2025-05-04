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


if selected_years:
    filtered_data = filtered_data[filtered_data['year'].isin(selected_years)]

if selected_violence:
    filtered_data = filtered_data[filtered_data['type_of_violence'].isin(selected_violence)]

if selected_side_a:
    filtered_data = filtered_data[filtered_data['side_a'].isin(selected_side_a)]

if selected_side_b:
    filtered_data = filtered_data[filtered_data['side_b'].isin(selected_side_b)]

if selected_regions:
    filtered_data = filtered_data[filtered_data['adm_1'].isin(selected_regions)]

st.write("### Filtered Data")
st.dataframe(filtered_data)


