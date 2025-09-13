import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Healthcare Provider Distribution Histograms")

df_variables = st.session_state["df_variables"]
df_origin = st.session_state["df_origin"]

tab1, tab2= st.tabs(['payer_code', 'medical_specialty'])

with tab1:
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['payer_code'], bins=5, color='skyblue')
    plt.title('Payer Code Count Distribution')
    plt.xlabel('Payer Code')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)

with tab2:
    unique_specialties = df_origin['medical_specialty'].dropna().unique()
    n=2
    split_arrays_specialties = np.array_split(unique_specialties, n)
    list_of_df=[]
    for i in range(n):
        list_of_df.append(df_origin[df_origin['medical_specialty'].isin(split_arrays_specialties[i])])

    fig,axes=plt.subplots(n,1,figsize=(10, 6*n))
    for i in range(n):
        sns.histplot(list_of_df[i]['medical_specialty'], ax=axes[i], color='lightblue')
        axes[i].tick_params(axis='x', labelrotation=90)
        axes[i].set_title(f'Subset {i+1} Medical Specialty Count Distribution')
    plt.tight_layout() 
    st.pyplot(plt)
