import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image



st.success('# EXPLORATORY DATA ANALYSIS 🎡')

df = pd.read_csv('C:/Users\HP/Desktop/streamlit_project/Customer-Churn-Records.csv', index_col='RowNumber')
st.success('### Taking a cursory look')
st.write(df.head())
st.write('No Of Rows and Columns')
st.write(df.shape)


options = ['Gender', 'Geography','Complain', 'Tenure', 'Card Type', 'HasCrCard','Satisfaction Score']
selected_option = st.selectbox('Distribution of some key features', options)
fig, ax = plt.subplots(figsize=(10, 8))
sns.countplot(data=df, x=selected_option)
st.pyplot(fig)

st.success('### Relationship Heatmap')
numeric_data = df.select_dtypes(include=[int, float])
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(numeric_data.corr(), annot=True, fmt='.2f', cmap='coolwarm', ax=ax)
st.pyplot(fig)

st.success('### Distribution of Exited Column (i.e. the target column)')
exit = df[df['Exited'] == 1]
not_exit = df[df['Exited'] == 0]
label = df['Exited'].unique()
height = (len(exit), len(not_exit))

fig, ax = plt.subplots()
ax.bar(label, height, color='grey')

# Customize the plot (optional)
plt.xticks(label,['Exits', 'Non Exits'])
plt.ylabel('No of Observations')
plt.title('Distribution of Exited Column')
st.pyplot(fig)

churn_rate = df[df['Exited']==1]
new_options = ['Gender', 'Geography','Complain', 'Tenure', 'Card Type', 'Satisfaction Score','HasCrCard']
selected_option = st.selectbox('**Select an option to show distribution of Exits per key feature:**', new_options)
fig, ax = plt.subplots(figsize=(10, 8))
sns.countplot(data=churn_rate, x=selected_option)
st.pyplot(fig)

    