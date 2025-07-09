import pandas as pd
import streamlit as st
#set title
st.title("Sensor Dashboard")
#get columns from sensor data
df = pd.read_csv('sensor_data.csv')
df.columns = df.columns.str.lower()
df = df.set_index("timestamp")
#get the last row
last_row = df.tail(1)
print(last_row.columns)

#set up columns
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("🌡️ Temp( C°)", f"{last_row['temperature'].values[0]}")

with col2:
    st.metric("💧 Humidity (%)",f"{last_row['humidity'].values[0]}")

with col3:
    st.metric("💨 Air Pressure (hPa)", f"{last_row['air pressure'].values[0]}")

with col4:
    st.metric("💡 Light Levels (lux)", f"{last_row['light'].values[0]}")

with col5:
    motion = "Yes" if last_row['motion'].values[0] else "No"
    st.metric("🏃‍♂️ Motion", motion)

#display data with charts for data analysis
st.subheader("Sensor Trends")
st.line_chart(df[["temperature", "humidity", "air pressure", "light"]]) #No motion b/c it returns boolean