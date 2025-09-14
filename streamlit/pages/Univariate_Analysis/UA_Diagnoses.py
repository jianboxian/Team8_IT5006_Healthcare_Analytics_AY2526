import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Diagnosis Distribution Histograms")

df_variables = st.session_state["df_variables"]
df_origin = st.session_state["df_origin"]

tab1, tab2, tab3= st.tabs(['dia_1', 'diag_2', 'diag_3'])

with tab1:
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='diag_1']['description']}")
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['diag_1'], bins=5, color='skyblue')
    plt.title('Diagnosis 1 Count Distribution')
    plt.xlabel('Diagnosis 1')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)
with tab2:
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='diag_2']['description']}")
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['diag_2'], bins=5, color='skyblue')
    plt.title('Diagnosis 2 Count Distribution')
    plt.xlabel('Diagnosis 2')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)
with tab3:
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='diag_3']['description']}")
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['diag_3'], bins=5, color='skyblue')
    plt.title('Diagnosis 3 Count Distribution')
    plt.xlabel('Diagnosis 3')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)
