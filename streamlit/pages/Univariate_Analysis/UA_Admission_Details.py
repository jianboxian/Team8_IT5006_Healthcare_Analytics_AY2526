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
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='admission_type_id']['description']}")
    st.markdown(""" **Type of admission** : `1`:Emergency  `2`:Urgent  `3`:Elective  etc.""")
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['admission_type_id'], bins=5, color='skyblue')
    plt.title('Admission Type Id Count Distribution')
    plt.xlabel('Admission Type Id')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)

with tab2:
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='discharge_disposition_id']['description']}")
    st.markdown(""" **Discharge destination** : `1`:Home  `3`:SNF  `6`:Home with service  etc.""")
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['discharge_disposition_id'], bins=5, color='skyblue')
    plt.title('Discharge Disposition Id Count Distribution')
    plt.xlabel('Discharge Disposition Id')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)

with tab3:
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='admission_source_id']['description']}")
    st.markdown(""" **Source of admission** : `1`:Physician referral `7`:Emergency room  etc.""")
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['admission_source_id'], bins=5, color='skyblue')
    plt.xlabel('Admission Source Id')
    plt.ylabel('Count')
    plt.title('Admission Source Id Count Distribution')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

with tab4:
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='time_in_hospital']['description']}")
    st.markdown(""" **Number of days in hospital (1-14 days)** """)
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['time_in_hospital'], bins=5, color='skyblue')
    plt.xlabel('Time in Hospital')
    plt.ylabel('Count')
    plt.title('Time in Hospital Count Distribution')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)