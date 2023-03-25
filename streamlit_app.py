import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Let's explore cars!")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)

cars_eu = df_cars.loc[df_cars['continent'] == 'Europe.']
cars_us = df_cars.loc[df_cars['continent'] == 'US.']
cars_jp = df_cars.loc[df_cars['continent'] == 'Japan.']

continents = [' ','US','Europe','Japan','All Regions']
dropdown = st.selectbox('Select a Region:', continents)
st.write('**You have selected:**',dropdown)

if dropdown == 'Europe':
  cars_eu
  viz_correlation_eu = sns.heatmap(cars_eu.corr(),
                                   center=0,
                                   cmap = sns.color_palette("vlag", as_cmap=True)
                                  )
  plt.title("HeatMap Europe")
  st.pyplot(viz_correlation_eu.figure)
  
if dropdown == 'US':
  cars_us
  viz_correlation_us = sns.heatmap(cars_us.corr(),
                                   center=0,
                                   cmap = sns.color_palette("vlag", as_cmap=True)
                                  )
  plt.title("HeatMap US")
  st.pyplot(viz_correlation_us.figure)
  
if dropdown == 'Japan':
  cars_jp
  viz_correlation_jp = sns.heatmap(cars_jp.corr(),
                                   center=0,
                                   cmap = sns.color_palette("vlag", as_cmap=True)
                                  )
  plt.title("HeatMap Japan")
  st.pyplot(viz_correlation_jp.figure)

if dropdown == 'All Regions':
  df_cars
  viz_correlation = sns.heatmap(df_cars.corr(),
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
#  st.pyplot(weight_hp_corr.figure)
