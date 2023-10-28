import streamlit as st
import pandas as pd

st.success('# IN THE FINAL ANALYSIS 🛒')
st.subheader('The project needs improvement!!!')
st.write(" #### Let's see the raw data again")
if st.button('View'):
    df = pd.read_csv('C:/Users\HP/Desktop/streamlit_project/Customer-Churn-Records.csv', index_col='RowNumber')
    col_rearrange = [col for col in df.columns if col != 'Exited'] + ['Exited']
    df = df.reindex(columns=col_rearrange)
    st.write(df.head())
st.success('### Ways to improve the project')
st.write(' * #### Collect more data about complaints detailing :')
st.write(' 1. When complaints were made and how long it took to resolve them')
st.write(' 2. Complaints resolution ratings')
st.write(' 3. The time beteen when a customer made a complaint and when they eventually left')

st.write(' * #### Create new columns from additional info detailed above')
st.write(' * #### Could also try more advanced models')
st.write(' * #### Carry out some hyperparameter tunning')

if st.button("Contact Information"):
    st.write("Name:  Saheed Salawu")
    st.write("Email: toorera@yahoo.co.uk")
    st.write("Phone: +234-08093023222")
    st.write('github: https://github.com/toorera')
