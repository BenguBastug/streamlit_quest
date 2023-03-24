import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Let's explore cars!")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)
df_cars


continents = ['US','Europe','Japan']
dropdown = st.radio('Select a Region:', continents)
st.write('**You have selected:**',dropdown)

weight_hp_corr = sns.scatterplot(data = df_cars[df_cars.continent==dropdown],
                                 x = 'weightlbs',
                                 y = 'hp',
                                 hue = 'year',
                                 size = 'cylinders',
                                 palette = 'coolwarm'
                                )
plt.title("Weight-Hp")
st.pyplot(weight_hp_corr.figure)


#viz_correlation = sns.heatmap(df_cars.corr(),
#                              center=0,
#                              cmap = sns.color_palette("vlag", as_cmap=True)
#                             )
#plt.title("HeatMap")
#st.pyplot(viz_correlation.figure)

