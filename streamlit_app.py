import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title and introductory text
st.title('Interactive Sales Dashboard')
st.write('This dashboard allows you to view sales data by year.')

# Sample data creation
data = {
    'Year': [2010, 2011, 2012, 2013, 2014, 2015],
    'Region': ['North', 'South', 'East', 'West', 'Central', 'North'],
    'Sales Amount': [200, 210, 220, 230, 240, 250]
}
df = pd.DataFrame(data)

# Slider widget for selecting a year
selected_year = st.slider('Select a year', min_value=2010, max_value=2015, value=2013)

# Display data for the selected year
st.write(f"Data for the year {selected_year}:")
filtered_df = df[df['Year'] == selected_year]
st.write(filtered_df)

# Plotting sales data for the selected year
fig, ax = plt.subplots()
ax.bar(filtered_df['Region'], filtered_df['Sales Amount'], color='skyblue')
plt.title(f'Sales in {selected_year}')
plt.xlabel('Region')
plt.ylabel('Sales Amount')
st.pyplot(fig)
