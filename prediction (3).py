import streamlit as st
import pandas as pd
import numpy as np
import sklearn
import pickle

model = pickle.load(open('/content/model.pkl', 'rb'))



st.title("Hemoglobin Prediction")
st.markdown(" This is a simple web application that predicts the Hemoglobin of your mobile phone based on the phone's specifications.")
st.markdown("The Hemoglobin are given as follows: ")
st.markdown(
"""
* Hit
* Not infected 

""")

#st.markdown("The data used for this project was collected from [Kaggle](https://www.kaggle.com/datasets/biswaranjanrao/anemia-dataset?select=anemia.csv
#)")
MCHC = st.number_input("Enter MCHC")
MCV = st.number_input("Enter MCV")
MCH = st.number_input("Enter MCH")

Hemoglobin = st.number_input("Enter Hemoglobin")
Gender = st.selectbox("Gender?",("Yes","No"))
if Gender == "Yes":
    Gender = 1
else:
    Gender = 0



hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

data = [[	Gender,Hemoglobin,MCH,MCHC,MCV]]

result = model.predict(data)

if Hemoglobin  >= 14:
    result_2 = "Not infected "


else:
    result_2 = "Fit"

if st.button('Submit'):
     st.write(" {}".format(result_2))
else:
     st.write('')
