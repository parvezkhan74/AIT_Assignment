import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data():
    df = pd.read_csv("cleaned_dataset.csv").iloc[:,1:]
    return df

df = load_data()

st.title('Bivariate Analysis')

num_cols = ['age', 'income', 'experience']
cat_cols = ['job_category', 'remote','country', 'gender','marital_status',
            'employment_status', 'analytics', 'dashboard']
all_cols = num_cols + cat_cols
col_dict = {'age': 'Age', 'income': 'Income', 'job_category': 'Job Category', 'remote': 'Remote',
            'country': 'Country','gender': 'Gender','marital_status': 'Marital Status', 'employment_status': 'Employment Status', 
            'experience': 'Experience', 'analytics': 'Analytical Skill', 'dashboard': 'Dashboard Skill'}

col1 = st.selectbox("Select fisrt column", all_cols)
col2 = st.selectbox("Select second column", [col for col in all_cols if col != col1])

if col1 in num_cols:
    type1 = 'numeric'
else:
    type1 = 'categoric'

if col2 in num_cols:
    type2 = 'numeric'
else:
    type2 = 'categoric'
    

fig, ax = plt.subplots()

if type1 == 'numeric' and type2 == 'numeric':
    st.subheader("Scatter Plot")
    sns.scatterplot(data = df, x = col1, y = col2, ax = ax)
    st.pyplot(fig)

elif type1 == 'categoric' and type2 == 'numeric':
    st.subheader("Box Plot")
    sns.boxplot(data = df, x = col1, y = col2, ax = ax)
    ax.set_xticklabels(ax.get_xticklabels(), rotation = 45)
    st.pyplot(fig)

elif type1 == 'numeric' and type2 == 'categoric':
    st.subheader("Box Plot")
    sns.boxplot(data = df, x = col2, y = col1, ax = ax)
    ax.set_xticklabels(ax.get_xticklabels(), rotation = 45)
    st.pyplot(fig)

elif type1 == 'categoric' and type2 == 'categoric':
    st.subheader("Count Plot (Grouped)")
    grouped = df.groupby([col1, col2]).size().reset_index(name = 'count')
    sns.barplot(data = grouped, x = col1, y = 'count', hue = col2, ax = ax)
    ax.set_xticklabels(ax.get_xticklabels(), rotation = 45)
    st.pyplot(fig)
