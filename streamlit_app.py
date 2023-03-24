import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Let's explore cars!")
st.write('And decide which one is better for us')

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df = pd.read_csv(link)
df

viz_correlation = sns.heatmap(df.corr(),
                              center=0,
                              cmap = sns.color_palette("vlag", as_cmap=True)
                             )
plt.title("HeatMap")
st.pyplot(viz_correlation.figure)

