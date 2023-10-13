import streamlit as st
import pandas as pd
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from sklearn.utils import resample


st.success('# MACHINE LEARNING AND CLASSIFICATION PHASE 👓')
st.subheader('Linear Regression was used to make prediction for this project')

df = pd.read_csv('C:/Users\HP/Desktop/streamlit_project/Customer-Churn-Records.csv', index_col='RowNumber')
df['card_type_code'] = df['Card Type'].astype('category').cat.codes
df['geography_code'] = df['Geography'].astype('category').cat.codes
df['gender_code'] = df['Gender'].astype('category').cat.codes

new_col = df[['Geography','Gender','Card Type','card_type_code','geography_code','gender_code']]

col_rearrange = [col for col in df.columns if col != 'Exited'] + ['Exited']
df = df.reindex(columns=col_rearrange)

exit = df[df['Exited'] == 1]
not_exit = df[df['Exited'] == 0]
label = df['Exited'].unique()
height = (len(exit), len(not_exit))

exit_upsampled = resample(exit, replace=True, n_samples=len(not_exit), random_state=27)
upsampled = pd.concat([not_exit, exit_upsampled])
upsampled_height = [len(upsampled[upsampled['Exited']==0]), len(upsampled[upsampled['Exited']==1])]

predictors = upsampled.columns[~upsampled.columns.isin(['CustomerId', 'Surname','Geography', 'Gender', 'Card Type', 'Exited'])]
upsampled = upsampled.sort_index(ascending = True)
upsampled.index = range(0, upsampled.shape[0], 1)










p = st.multiselect('Predictors', predictors, placeholder='Select Feature',default='Age')
    
st.success('Accuracy Score')
x = upsampled[p]
y = upsampled['Exited']
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.2, random_state=50)
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(X_train, y_train)
lr_predict = lr.predict(X_test)

from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score


predictions = accuracy_score(y_test, lr_predict)
st.text(predictions)

if st.button('View the result'):
    j = pd.Series(lr_predict, index=y_test.index)
    k = pd.concat((y_test, j), axis=1)
    k.columns = ['Actual', 'Predictions']
    st.write(k)

if st.button('Congrats!!!'):
    st.balloons()