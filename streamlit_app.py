import streamlit as st
import pandas as pd

st.title('Hello Wilders, welcome to my application!')
st.write("I enjoy to discover streamlit possibilities")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/weather2019.csv"

df_weather = pd.read_csv(link)

st.write(df_weather)
