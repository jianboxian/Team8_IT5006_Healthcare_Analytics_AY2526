import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Medication Distribution Histograms")

df_variables = st.session_state["df_variables"]
df_origin = st.session_state["df_origin"]
glipizide = df_origin['glipizide']
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(['metformin', 'repaglinide','nateglinide','chlorpropamide','glimepiride','glipizide','glyburide','pioglitazone','rosiglitazone','insulin'])

with tab1:
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['metformin'], bins=5, color='skyblue')
    plt.title('Metformin Count Distribution')
    plt.xlabel('Metformin')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)
with tab2:
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['repaglinide'], bins=5, color='skyblue')
    plt.title('Repaglinide Count Distribution')
    plt.xlabel('Repaglinide')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)  
with tab3:
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['nateglinide'], bins=5, color='skyblue')
    plt.title('Nateglinide Count Distribution')
    plt.xlabel('Nateglinide')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)
with tab4:
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['chlorpropamide'], bins=5, color='skyblue')
    plt.title('Chlorpropamide Count Distribution')
    plt.xlabel('Chlorpropamide')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)
with tab5:
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['glimepiride'], bins=5, color='skyblue')
    plt.title('Glimepiride Count Distribution')
    plt.xlabel('Glimepiride')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)
with tab6:
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['glipizide'], bins=5, color='skyblue')
    plt.title('Glipizide Count Distribution')
    plt.xlabel('Glipizide')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)
with tab7:
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['glyburide'], bins=5, color='skyblue')
    plt.title('Glyburide Count Distribution')
    plt.xlabel('Glyburide')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)
with tab8:
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['pioglitazone'], bins=5, color='skyblue')
    plt.title('Pioglitazone Count Distribution')
    plt.xlabel('Pioglitazone')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)
with tab9:
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['rosiglitazone'], bins=5, color='skyblue')
    plt.title('Rosiglitazone Count Distribution')
    plt.xlabel('Rosiglitazone')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)
with tab10:
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['insulin'], bins=5, color='skyblue')
    plt.title('Insulin Count Distribution')
    plt.xlabel('Insulin')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)