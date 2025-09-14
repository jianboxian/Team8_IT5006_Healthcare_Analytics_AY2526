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
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='age']['description']}")
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['age'], bins=5, color='skyblue')
    plt.title('Age Count Distribution')
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)

with tab2:
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='gender']['description']}")
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['gender'], bins=5, color='skyblue')
    plt.title('Gender Count Distribution')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)

with tab3:
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='race']['description']}")
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['race'], bins=5, color='skyblue')
    plt.xlabel('Race')
    plt.ylabel('Count')
    plt.title('Race Count Distribution')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

with tab4:
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='weight']['description']}")
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['weight'], bins=5, color='skyblue')
    plt.xlabel('Weight')
    plt.ylabel('Count')
    plt.title('Weight Count Distribution')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)