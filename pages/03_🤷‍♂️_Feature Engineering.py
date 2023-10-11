import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.utils import resample

df = pd.read_csv('C:/Users\HP/Desktop/streamlit_project/Customer-Churn-Records.csv', index_col='RowNumber')

st.success('# DATA PRE-PROCESSING PHASE🍳')
st.subheader('This is the section where the dataset is pre-processed preparatory to the data modeling and prediction stage')
st.write('Some of the activities carried out at this stage might include:')
st.markdown('* Changing of data type')
st.markdown('* Creation of new columns and/or rows')
st.markdown('* Elimination of unwanted columns and/or rows')
st.markdown('* Resampling of unbalanced target feature')
st.markdown('* and many more........')

st.write('In this project however, the following importatnt columns need to be converted from object datatype to integer because most machine learning algorithms do not work with text data')
st.success('## Below are the affected columns')
subset = df[['Geography', 'Gender', 'Card Type']]
st.write(subset)

df['card_type_code'] = df['Card Type'].astype('category').cat.codes
df['geography_code'] = df['Geography'].astype('category').cat.codes
df['gender_code'] = df['Gender'].astype('category').cat.codes

st.success('## Here are the new columns created')
new_col = df[['Geography','Gender','Card Type','card_type_code','geography_code','gender_code']]
st.write(new_col)

col_rearrange = [col for col in df.columns if col != 'Exited'] + ['Exited']
df = df.reindex(columns=col_rearrange)
st.success('#### Columns rearranged to push the target column - Exited - to the exreme right in alignment with best practice')
if st.button('Check it out'):
    st.write(df.head())

st.subheader('Resampling of target column')

exit = df[df['Exited'] == 1]
not_exit = df[df['Exited'] == 0]
label = df['Exited'].unique()
height = (len(exit), len(not_exit))
st.success('## Here is the initial distribution')
fig, ax = plt.subplots()
ax.bar(label, height, color='grey')

# Customize the plot (optional)
plt.xticks(label,['Exits', 'Non Exits'])
plt.ylabel('No of Observations')
plt.title('Distribution of Exited Column')
st.pyplot(fig)

exit_upsampled = resample(exit, replace=True, n_samples=len(not_exit), random_state=27)
upsampled = pd.concat([not_exit, exit_upsampled])
upsampled_height = [len(upsampled[upsampled['Exited']==0]), len(upsampled[upsampled['Exited']==1])]

st.success('## Now Target Column Resampled 👇👇👇')
fig, ax = plt.subplots()
ax.bar(label, upsampled_height, color='orange')
ax.bar(label, height, color='green')
plt.xticks(label,['Exits', 'Non Exits'])
plt.ylabel('No of observations')
plt.legend(['resampled','original'])
st.pyplot(fig)
