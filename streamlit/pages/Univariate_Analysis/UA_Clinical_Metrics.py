import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Clinical Metrics Distribution Histograms")

df_variables = st.session_state["df_variables"]
df_origin = st.session_state["df_origin"]

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(['num_lab_procedures', 'num_procedures', 'num_medications','number_outpatient','number_emergency','number_inpatient','number_diagnoses'])


with tab1:
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['num_lab_procedures'], color='skyblue', kde=True)
    plt.title(f'Number of Lab Procedures Count Distribution | Skewness: {df_origin["num_lab_procedures"].skew():.2f} | Kurtosis: {df_origin["num_lab_procedures"].kurtosis():.2f}')
    plt.xlabel('Number of Lab Procedures')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)

with tab2:
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['num_procedures'], color='skyblue', kde=True)
    plt.title(f'Number of Procedures Count Distribution | Skewness: {df_origin["num_procedures"].skew():.2f} | Kurtosis: {df_origin["num_procedures"].kurtosis():.2f}')
    plt.xlabel('Number of Procedures')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)

with tab3:
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['num_medications'], color='skyblue', kde=True)
    plt.title(f'Number of Medications Count Distribution | Skewness: {df_origin["num_medications"].skew():.2f} | Kurtosis: {df_origin["num_medications"].kurtosis():.2f}')
    plt.xlabel('Number of Medications')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)

with tab4:
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['number_outpatient'], color='skyblue', kde=True)
    plt.title(f'Number of Outpatient Visits Count Distribution | Skewness: {df_origin["number_outpatient"].skew():.2f} | Kurtosis: {df_origin["number_outpatient"].kurtosis():.2f}')
    plt.xlabel('Number of Outpatient Visits')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)

with tab5:
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['number_emergency'], color='skyblue', kde=True)
    plt.title(f'Number of Emergency Visits Count Distribution | Skewness: {df_origin["number_emergency"].skew():.2f} | Kurtosis: {df_origin["number_emergency"].kurtosis():.2f}')
    plt.xlabel('Number of Emergency Visits')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)

with tab6:
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['number_inpatient'], color='skyblue', kde=True)
    plt.title(f'Number of Inpatient Visits Count Distribution | Skewness: {df_origin["number_inpatient"].skew():.2f} | Kurtosis: {df_origin["number_inpatient"].kurtosis():.2f}')
    plt.xlabel('Number of Inpatient Visits')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)

with tab7:
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['number_diagnoses'], color='skyblue', kde=True)
    plt.title(f'Number of Diagnoses Count Distribution, | Skewness: {df_origin["number_diagnoses"].skew():.2f} | Kurtosis: {df_origin["number_diagnoses"].kurtosis():.2f}')
    plt.xlabel('Number of Diagnoses')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)

