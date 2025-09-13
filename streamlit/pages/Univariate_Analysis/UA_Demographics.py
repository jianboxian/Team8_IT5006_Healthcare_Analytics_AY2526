import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Demographic Distribution Histograms")

df_variables = st.session_state["df_variables"]
df_origin = st.session_state["df_origin"]

tab1, tab2, tab3, tab4 = st.tabs(['Age', 'Gender', 'Race','Weight'])

with tab1:
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['age'], bins=5, color='skyblue')
    plt.title('Age Count Distribution')
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)

with tab2:
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['gender'], bins=5, color='skyblue')
    plt.title('Gender Count Distribution')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)

with tab3:
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['race'], bins=5, color='skyblue')
    plt.xlabel('Race')
    plt.ylabel('Count')
    plt.title('Race Count Distribution')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

with tab4:
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['weight'], bins=5, color='skyblue')
    plt.xlabel('Weight')
    plt.ylabel('Count')
    plt.title('Weight Count Distribution')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)