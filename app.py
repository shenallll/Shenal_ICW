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

# Visualizations
st.write("#Visualizations")

# 1. Total Deaths by Year - Line Chart
st.subheader("Total Deaths by Year")
deaths_by_year = filtered_data.groupby("year")["best"].sum().reset_index()
fig = px.line(deaths_by_year, x="year", y="best", title="Total Deaths by Year")
st.plotly_chart(fig)

# 2. Number of Events by Region - Horizontal Bar Chart
st.subheader("Number of Events by Region")
events_by_region = filtered_data['adm_1'].value_counts().reset_index()
events_by_region.columns = ['Region', 'Event Count']
fig = px.bar(events_by_region, x="Event Count", y="Region", orientation='h', title="Number of Events by Region")
st.plotly_chart(fig)

# 3. Events by Type of Violence - Pie Chart
st.subheader("Events by Type of Violence")
events_by_type = filtered_data['type_of_violence'].value_counts().reset_index()
events_by_type.columns = ['Type of Violence', 'Count']
fig = px.pie(events_by_type, names='Type of Violence', values='Count', title="Events by Type of Violence")
st.plotly_chart(fig)

# 4. Conflict Events Location Map
st.subheader("Conflict Events Location Map")
map_data = filtered_data[['latitude', 'longitude']].dropna()
if not map_data.empty:
    st.map(map_data)
else:
    st.write("No location data available for selected filters.")

# 5. Total Deaths by Side A - Horizontal Bar Chart
st.subheader("Total Deaths by Side A")
deaths_by_side_a = filtered_data.groupby("side_a")["best"].sum().reset_index().sort_values(by="best", ascending=False)
fig = px.bar(deaths_by_side_a, x="best", y="side_a", orientation='h', title="Total Deaths by Side A")
st.plotly_chart(fig)

# 6. Events over Time - Line Chart
st.subheader("Events over Time")
filtered_data["date_start"] = pd.to_datetime(filtered_data["date_start"], errors='coerce')
events_over_time = filtered_data.groupby("date_start").size().reset_index(name='Event Count')
fig = px.line(events_over_time, x="date_start", y="Event Count", title="Events over Time")
st.plotly_chart(fig)



