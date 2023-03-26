import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Let's explore cars!")
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df = pd.read_csv(link)

#cars_eu = df[df['continent'] == 'Europe.']
#cars_us = df[df['continent'] == 'US.']
#cars_jp = df[df['continent'] == 'Japan.']

continents = ['US','Europe','Japan','All Regions']
region = st.sidebar.selectbox('Select Region:', continents)

if region == 'Europe':
  df = df[df['continent'] == 'Europe.']
  viz_correlation_eu = sns.heatmap(df.corr(),
                                   center=0,
                                   cmap = sns.color_palette("vlag", as_cmap=True)
                                  )
  plt.title("HeatMap Europe")
  st.pyplot(viz_correlation_eu.figure)

if region == 'US':
  df = df[df['continent'] == 'US.']
  viz_correlation_us = sns.heatmap(df.corr(),
                                   center=0,
                                   cmap = sns.color_palette("vlag", as_cmap=True)
                                  )
  plt.title("HeatMap US")
  st.pyplot(viz_correlation_us.figure)

if region == 'Japan':
  df = df[df['continent'] == 'Japan.']
  viz_correlation_jp = sns.heatmap(df.corr(),
                                   center=0,
                                   cmap = sns.color_palette("vlag", as_cmap=True)
                                  )
  plt.title("HeatMap Japan")
  st.pyplot(viz_correlation_jp.figure)

if dropdown == 'All Regions':
  df
  viz_correlation = sns.heatmap(df.corr(),
                                center=0,
                                cmap = sns.color_palette("vlag", as_cmap=True)
                                )
  plt.title("HeatMap All Regions")
  st.pyplot(viz_correlation.figure)


#  viz_corr = sns.scatterplot(data = df_cars[df_cars['continent']==dropdown],
#                                   x = 'weightlbs',
#                                   y = 'hp',
#                                   hue = 'year',
#                                   size = 'cylinders',
#                                   palette = 'coolwarm'
#                                  )
#  plt.title("Weight-Hp")
# st.pyplot(weight_hp_corr.figure)
