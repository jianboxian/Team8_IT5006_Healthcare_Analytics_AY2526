import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Laboratory Results Distribution Histograms")

df_variables = st.session_state["df_variables"]
df_origin = st.session_state["df_origin"]

tab1, tab2 = st.tabs(['max_glu_serum', 'A1Cresult'])

with tab1:
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='max_glu_serum']['description']}")
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['max_glu_serum'], bins=5, color='skyblue')
    plt.title('Max Glucose Serum Count Distribution')
    plt.xlabel('Max Glucose Serum')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)

with tab2:
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='A1Cresult']['description']}")
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['A1Cresult'], bins=5, color='skyblue')
    plt.title('A1C Result Count Distribution')
    plt.xlabel('A1C Result')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)