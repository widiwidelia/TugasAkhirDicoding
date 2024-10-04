import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Dashboard Penyewaan Sepeda')
st.caption('Angela Sekar Widelia ML-65')

hour_df = pd.read_csv('hour.csv')  
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
hour_df['weekday'] = hour_df['dteday'].dt.weekday

# Pertanyaan 1
by_hour = hour_df.groupby(by="hr").agg({
    "cnt": ["sum","mean"],
    "registered": ["sum","mean"],
    "casual" : ["sum","mean"]
}).sort_values(by="hr", ascending=True)

st.header('Jumlah Penyewaan Sepeda pada Setiap Jam')

plt.figure(figsize=(10,6))
fig, ax = plt.subplots()
sns.barplot(x='hr', y='cnt', data=hour_df, palette="pastel")
plt.xlabel('Jam dalam 24-hour format')
plt.ylabel('Jumlah penyewaan')
st.pyplot(fig)

st.caption('Jam dengan penyewaan tertinggi adalah jam 17.00, dengan jumlah penyewaan mencapai 336860.')

# Pertanyaan 2
by_day = hour_df.groupby('weekday')['cnt'].sum().reset_index()
by_day['weekday'] = by_day['weekday'].replace({
    0: 'Sun',
    1: 'Mon',
    2: 'Tue',
    3: 'Wed',
    4: 'Thu',
    5: 'Fri',
    6: 'Sat'
})

st.header('Jumlah Penyewaan Sepeda Setiap Hari dalam Satu Pekan')

plt.figure(figsize=(10, 6))
fig, ax = plt.subplots()
sns.barplot(x='weekday', y='cnt', data=by_day, palette='pastel')
plt.xlabel('Hari dalam satu pekan')
plt.ylabel('Jumlah penyewaan')
st.pyplot(fig)

st.caption('Hari dengan penyewaan tertinggi adalah hari Kamis.')
