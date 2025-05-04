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



# Sidebar Filters
st.sidebar.header("Filter the Data")

# Year filter
years = data['year'].unique()
selected_years = st.sidebar.multiselect("Select Year", sorted(years))

# Type of Violence filter
violence_types = data['type_of_violence'].unique()
selected_violence = st.sidebar.multiselect("Select Type of Violence", sorted(violence_types))

# Side A filter
side_a = data['side_a'].unique()
selected_side_a = st.sidebar.multiselect("Select Side A", sorted(side_a))

# Side B filter
side_b = data['side_b'].unique()
selected_side_b = st.sidebar.multiselect("Select Side B", sorted(side_b))

# Region filter
regions = data['adm_1'].unique()
selected_regions = st.sidebar.multiselect("Select Region", sorted(regions))

# Apply filters
filtered_data = data.copy()

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

