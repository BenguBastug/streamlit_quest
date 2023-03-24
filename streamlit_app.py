import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Let's explore cars!")
st.write('And decide which one is better for us')

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)
df_cars

weight_hp_corr = sns.scatterplot(data = df_cars,
                                 x = 'weightlbs',
                                 y = 'hp',
                                 hue = 'year',
                                 size = 'cylinders',
                                 palette = 'coolwarm'
                                )
plt.title("Weight-Hp")
st.pyplot(weight_hp_corr.figure)


viz_correlation = sns.heatmap(df_cars.corr(),
                              center=0,
                              cmap = sns.color_palette("vlag", as_cmap=True)
                             )
plt.title("HeatMap")
st.pyplot(viz_correlation.figure)


continents = ('US','Europe','Japan')
dropdown = st.selectbox('Select a Region:', continents)
mean_value_table = df_cars.groupby(continents).mean()


