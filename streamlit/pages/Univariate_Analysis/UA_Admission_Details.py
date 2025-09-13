import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Admission Details Distribution Histograms")

df_variables = st.session_state["df_variables"]
df_origin = st.session_state["df_origin"]

tab1, tab2, tab3, tab4 = st.tabs(['admission_type_id', 'discharge_disposition_id', 'admission_source_id','time_in_hospital'])

with tab1:
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['admission_type_id'], bins=5, color='skyblue')
    plt.title('Admission Type Id Count Distribution')
    plt.xlabel('Admission Type Id')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)

with tab2:
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['discharge_disposition_id'], bins=5, color='skyblue')
    plt.title('discharge_disposition_id Count Distribution')
    plt.xlabel('Discharge Disposition Id')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)

with tab3:
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['admission_source_id'], bins=5, color='skyblue')
    plt.xlabel('Admission Source Id')
    plt.ylabel('Count')
    plt.title('Admission Source Id Count Distribution')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

with tab4:
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['time_in_hospital'], bins=5, color='skyblue')
    plt.xlabel('Time in Hospital')
    plt.ylabel('Count')
    plt.title('Time in Hospital Count Distribution')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)