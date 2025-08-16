import streamlit as st 
import pandas as pd 
import pickle 
st.set_page_config(page_title='Car_Price_Prediction',page_icon='home_icon.jpg')
st.header('Welcome to Mumbai Car Price Predictor:')
df=pd.read_csv('copied.csv')
with open('RFmodel.pkl','rb') as file:
    model=pickle.load(file)
with st.container(border=True):
    col1,col2=st.columns(2)
    year=col1.selectbox('Year',options=df['Year'].unique())
    fuel=col2.selectbox("Fuel Type",options=df['Fuel Type'].unique())
    mileage=col1.number_input("Mileage",min_value=5,step=10)
    price=col2.number_input("Price",min_value=10000,step=1000)
    fuels=list(df['Fuel Type'].unique())
    fuels.sort()
    input_values=[(fuels.index(fuel),year,mileage,price)]
    c1,c2,c3=st.columns([1.6,1.5,1])
    if c2.button('predict_price'):
        out=model.predict(input_values)
        st.subheader(f'Total_Price💰: {out[0]}')
