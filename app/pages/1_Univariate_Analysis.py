import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data():
    df = pd.read_csv("app/cleaned_dataset.csv").iloc[:,1:]
    return df

df = load_data()

st.title('Univariate Analysis')

num_cols = ['age', 'income']
cat_cols = ['job_category', 'remote','country', 'gender','marital_status',
            'employment_status', 'experience', 'analytics', 'dashboard']
all_cols = num_cols + cat_cols
col_dict = {'age': 'Age', 'income': 'Income', 'job_category': 'Job Category', 'remote': 'Remote',
            'country': 'Country','gender': 'Gender','marital_status': 'Marital Status', 'employment_status': 'Employment Status', 
            'experience': 'Experience', 'analytics': 'Analytical Skill', 'dashboard': 'Dashboard Skill'}

select_col = st.selectbox('Select a column', all_cols)

if select_col in num_cols:
    st.subheader('Column Summary')
    st.dataframe(pd.DataFrame(df[select_col].describe()).T, use_container_width = True)
    
    st.subheader('Column Distribution')
    fig, ax = plt.subplots()
    sns.histplot(df[select_col].dropna(), kde=True, bins=20, ax=ax)
    st.pyplot(fig)
    
elif select_col == 'experience':
    st.subheader('Column Summary')
    st.dataframe(pd.DataFrame(df[select_col].describe()).T, use_container_width = True)
    
    st.subheader('Column Distribution')
    fig, ax = plt.subplots()
    df[select_col].value_counts().sort_values(ascending = False).plot(kind = 'bar', xlabel = 'Experience', rot = 0)
    st.pyplot(fig)
    
elif select_col == 'country':
    st.subheader('Column Summary')
    st.dataframe(pd.DataFrame(df[select_col].value_counts()).T, use_container_width = True)
    
    st.subheader('Column Distribution')
    fig, ax = plt.subplots()
    df[select_col].value_counts().sort_values(ascending = False).head(10).plot(kind = 'bar', xlabel = ' Top 10 Country', rot = 45)
    st.pyplot(fig)
    
elif select_col in cat_cols:
    st.subheader('Column Summary')
    st.dataframe(pd.DataFrame(df[select_col].value_counts()).T, use_container_width = True)
    
    st.subheader('Column Distribution')
    fig, ax = plt.subplots()
    df[select_col].value_counts().plot(kind = 'pie', ylabel = '', autopct = '%0.1f%%', ax = ax)
    st.pyplot(fig)
