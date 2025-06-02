import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data():
    df = pd.read_csv("app/cleaned_dataset.csv").iloc[:,1:]
    return df

df = load_data()

st.title("Employee Data Dashboard")

st.subheader("Overview")

with st.expander("🔍 Show Raw Data"):
    st.dataframe(df)
    
col1, col2, col3 = st.columns(3)
col1.metric("Total Records", len(df))
col2.metric("Total Columns", df.shape[1])
col3.metric("Unique Countries", df['country'].nunique())

st.subheader("Descriptive Statistics (Numeric Columns)")
st.dataframe(df[['age', 'income', 'experience']].describe().T, use_container_width = True)

st.subheader("Categorical Distributions")
cat_cols = ['gender', 'marital_status', 'remote', 'employment_status', 'job_category', 'country', 'analytics', 'dashboard']
cat_col_labels = ['Gender', 'Marital Status', 'Country', 'Employment Status', 'Job Category', 'country', 'Analytical Skill', 'Dashboard Skill']

for i in range(3):
    cols = st.columns(3)
    j = 0
    while (3*i + j) < 8 and j < 3:
        
        with cols[j]:
            col = cat_cols[3*i + j]
            st.markdown(f"**{cat_col_labels[i*3 + j]}**")
            st.write(df[col].value_counts().head())
        j += 1
