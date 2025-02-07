import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load data
df = pd.read_csv('cleaned_data.csv')
df['datetime'] = pd.to_datetime(df['datetime'])

# Set up the dashboard title
st.title('Air Quality Dashboard')

# Sidebar for date input
st.sidebar.header('Filter by Date Range')
min_date = pd.to_datetime('2013-01-01')
max_date = pd.to_datetime('2017-12-31')
start_date = st.sidebar.date_input('Start date', min_value=min_date, max_value=max_date, value=min_date)
end_date = st.sidebar.date_input('End date', min_value=min_date, max_value=max_date, value=max_date)

df_filtered = df[(df['datetime'].dt.date >= start_date) & (df['datetime'].dt.date <= end_date)]

df_filtered['month'] = df_filtered['datetime'].dt.month
df_filtered['season'] = df_filtered['datetime'].dt.month % 12 // 3 + 1

# Create month and season columns
df['month'] = df['datetime'].dt.month
df['season'] = df['datetime'].dt.month % 12 // 3 + 1

# Visualization 1: Monthly trend of PM2.5 and PM10
st.subheader('Tren bulanan PM2.5 & PM10')
plt.figure(figsize=(10, 6))
sns.lineplot(data=df_filtered, x='month', y='PM2.5', label='PM2.5')
sns.lineplot(data=df_filtered, x='month', y='PM10', label='PM10')
plt.title('Monthly Trend of PM2.5 & PM10')
plt.xlabel('Month')
plt.ylabel('Concentration (µg/m³)')
plt.legend()
st.pyplot(plt)

# Visualization 2: Correlation heatmap
st.subheader('Korelasi antara Polutan PM2.5 & PM10 dengan Faktor Cuaca')
correlation = df_filtered[['PM2.5', 'PM10', 'TEMP', 'PRES', 'DEWP', 'RAIN', 'WSPM']].corr()
plt.figure(figsize=(10, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlation between Pollution and Weather Factors')
st.pyplot(plt)

# Filter data for the last three years
last_three_years = df_filtered['datetime'].dt.year.max() - 2
df_filtered_last_three_years = df_filtered[df_filtered['datetime'].dt.year >= last_three_years]

# Visualization 3: O3 exceedance by station
st.subheader('Pelanggaran Batas O3 per Stasiun')
df_filtered_last_three_years['O3_over'] = df_filtered_last_three_years['O3'] > 100
station_o3_exceed = df_filtered_last_three_years.groupby('station')['O3_over'].sum().reset_index()
station_o3_exceed.columns = ['station', 'exceed_days']
o3_sorted = station_o3_exceed.sort_values(by='exceed_days', ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(data=o3_sorted, x='station', y='exceed_days')
plt.title('Number of Days Exceeding O3 Standard (WHO: 100 µg/m³) per Station')
plt.xlabel('Station')
plt.ylabel('Number of Days')
plt.xticks(rotation=45)
st.pyplot(plt)

# Visualization 4: O3 exceedance trend over the last three years
st.subheader('Pelanngaran Batas O3 per Bulan')
df_filtered_last_three_years['year'] = df_filtered_last_three_years['datetime'].dt.year
o3_exceed_trend = df_filtered_last_three_years[df_filtered_last_three_years['O3_over']].groupby(['year', 'month']).size().reset_index(name='exceed_days')
plt.figure(figsize=(10, 6))
sns.lineplot(data=o3_exceed_trend, x='month', y='exceed_days', hue='year')
plt.title('O3 Exceedance Trend per Month')
plt.xlabel('Month')
plt.ylabel('Number of Days Exceeding Limit')
st.pyplot(plt)