import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets

st.write("""
# Simple Iris Flower prediction app
         

This app predicts the iris flower type

""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal Lenght', 4.3,7.9,5.4)
    sepal_width = st.sidebar.slider("Sepal Width", 2.0,4.4,3.4)
    petal_length = st.sidebar.slider("Petal Lenght",1.0,6.9,1.3)
    petal_width = st.sidebar.slider("Petal Width",0.1,2.5,0.2)

    data = {
        'sepal_length': sepal_length,
        'sepal_width': sepal_width,
        'petal_lenght': petal_length,
        'petal_width': petal_width
    }
    features = pd.DataFrame(data,index=[0])
    return features


df = user_input_features()

st.subheader("User Input Parameters")
st.write(df)

iris = datasets.load_iris()
X = iris.data
Y = iris.target

clf = RandomForestClassifier()
clf.fit(X,Y)

predictions = clf.predict(df)
predictions_prob = clf.predict_proba(df)

st.subheader('Class labels and theri cooresponding index labels')
st.write(iris.target_names)

st.write('Prediction Probabilituy')
st.write(predictions_prob)


st.write(iris.target_names[predictions])
