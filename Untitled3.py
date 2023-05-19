import pandas as pd
import streamlit as st
import plotly.express as px


st.set_page_config(page_title='Machine Learning Application')
st.header('Welcome to ML Application')

df=pd.read_csv("C:\\Users\\99451\\Downloads\\water_potability.csv")
data=pd.read_csv("C:\\Users\\99451\\Downloads\\loan_pred.csv")
st.dataframe(df)
st.dataframe(data)

chart2 =px.scatter(df,
                       
                   x='Solids',
                   y='Hardness',
                   color='Potability',
                   title='Scatter Plot')

st.plotly_chart(chart2)

chart1=px.pie(data,
              title='Pie Chart',
              names='CoapplicantIncome',
              values='Education',)

st.plotly_chart(chart1)
