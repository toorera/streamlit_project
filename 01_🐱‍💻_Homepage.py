import streamlit as st


st.set_page_config(
    page_title="Multipage App",
    page_icon="👏",
)


st.title("WELCOME TO CUSTOMER CHURN CLASSIFICATION PROJECT!!! 🐱‍💻")
if st.button('Project Aim'):
    st.write('The aim of this project is to use machine learning model to classify customers in the dataset into 2 categories i.e. Exits and Non-Exits')
if st.button('About the dataset'):
    st.markdown('* **Data Source**')
    st.write('The dataset used for this project was sourced from one of the projects on Kaggle platform')
    st.markdown('* **Link To The Dataset**')
    st.write('https://www.kaggle.com/datasets/radheshyamkollipara/bank-customer-churn?resource=download')

if st.button('Applicable Industries'):
    st.markdown('* **Banking**')
    st.markdown('* **Telecommunication**')
    st.markdown('* **Manufacturing**')
    st.markdown('* **ETC......**')
