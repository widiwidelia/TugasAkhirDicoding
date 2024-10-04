import streamlit as st

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Dashboard Penyewaan Sepeda')
st.caption('Angela Sekar Widelia ML-65')

hour_df = pd.read_csv('Data/hour.csv')  
day_df = pd.read_csv('Data/day.csv')  
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
hour_df['weekday'] = hour_df['dteday'].dt.weekday

# Pertanyaan 1
by_hour = hour_df.groupby("hr").agg({
    "cnt": ["sum","mean"],
    "registered": ["sum","mean"],
    "casual" : ["sum","mean"]
}).sort_values(by="hr", ascending=True)

st.header('Jumlah Penyewaan Sepeda pada Setiap Jam')

plt.figure(figsize=(10,6))
fig, ax = plt.subplots()
sns.barplot(x='hr', y='cnt', data=hour_df)
plt.xlabel('Jam dalam 24-hour format')
plt.ylabel('Jumlah penyewaan')
st.pyplot(fig)

st.caption('Jam dengan penyewaan tertinggi adalah jam 17.00, dengan jumlah penyewaan mencapai 336860.')

# Pertanyaan 2
by_day = day_df.groupby('weekday')['cnt'].sum().reset_index()
by_day['weekday'] = by_day['weekday'].map({
    0: 'Sunday',
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday'
})

st.header('Jumlah Penyewaan Sepeda Setiap Hari dalam Satu Pekan')

plt.figure(figsize=(10, 6))
fig, ax = plt.subplots()
sns.barplot(x='weekday', y='cnt', data=by_day)
plt.xlabel('Hari dalam satu pekan')
plt.ylabel('Jumlah penyewaan')
st.pyplot(fig)

st.caption('Hari dengan penyewaan tertinggi adalah hari Jumat.')
