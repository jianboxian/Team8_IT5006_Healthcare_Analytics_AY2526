import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Treatment Changes Distribution Histograms")

df_variables = st.session_state["df_variables"]
df_origin = st.session_state["df_origin"]

tab1, tab2= st.tabs(['change', 'diabetesMed'])

with tab1:
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['change'], bins=5, color='skyblue')
    plt.title('Change Count Distribution')
    plt.xlabel('Change')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)

with tab2:
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['diabetesMed'], bins=5, color='skyblue')
    plt.title('Diabetes Medication Count Distribution')
    plt.xlabel('Diabetes Medication')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)  
