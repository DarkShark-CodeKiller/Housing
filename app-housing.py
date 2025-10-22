import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()

# Title and Header
st.title('California Housing Data (1990) by Xinyan Li')

# Load the dataset
df = pd.read_csv('housing.csv')

# Sidebar Filters
HousingPrice_filter = st.slider('Minimal Median Housing Price:', 0, 500001, 20000)
locationtype_filter = st.sidebar.multiselect('Choose the location type', df.ocean_proximity.unique(), df.ocean_proximity.unique())
genre = st.sidebar.radio("Choose income level", ["Low", "Medium", "High"])

# Filtering Data
filtered_df = df[
    (df['median_house_value'] >= HousingPrice_filter) & 
    (df['ocean_proximity'].isin(locationtype_filter))
].copy()

# Income level filter
if genre == "Low":
    filtered_df = filtered_df[filtered_df['median_income'] <= 2.5]
elif genre == "Medium":
    filtered_df = filtered_df[(filtered_df['median_income'] > 2.5) & (filtered_df['median_income'] < 4.5)]
else: 
    filtered_df = filtered_df[filtered_df['median_income'] > 4.5]

# Map Plotting: Make sure to have latitude and longitude columns in your dataset
if 'latitude' in df.columns and 'longitude' in df.columns:
    st.map(filtered_df)

# Subheader for filters
st.subheader('See more filters in the sidebar')

# Histogram Plotting
st.subheader('Median House Value Histogram')
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(filtered_df['median_house_value'], bins=30, color='skyblue', edgecolor='black')
ax.set_xlabel('Median House Value')
ax.set_ylabel('Frequency')
ax.set_title('Distribution of Median House Value')
st.pyplot(fig)

