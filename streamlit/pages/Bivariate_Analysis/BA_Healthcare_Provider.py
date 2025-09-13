import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Healthcare Provider Distribution Histograms")

df_variables = st.session_state["df_variables"]
df_origin = st.session_state["df_origin"]
readmitted_statuses = df_origin['readmitted'].unique()


tab1, tab2= st.tabs(['payer_code', 'medical_specialty'])

with tab1:
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df_origin, x='payer_code', hue='readmitted', stat="count")
    plt.xlabel('Payer Code')
    plt.ylabel("Count")
    plt.title(f'Readmission Status By Payer Code')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

    payer_code_statuses = df_origin['payer_code'].dropna().unique()
    ncols = 4
    nrows = int(np.ceil(len(payer_code_statuses)/ncols))
    fig,axes=plt.subplots(nrows,ncols,figsize=(8*ncols, 8*nrows))
    if nrows <= 1:
        for i, status in enumerate(payer_code_statuses):
            subset = df_origin[df_origin['payer_code'] == status]
            payer_code_counts = subset['readmitted'].value_counts()
            axes[i].pie(payer_code_counts, labels=payer_code_counts.index, autopct='%1.1f%%', startangle=140)
            axes[i].set_title(f'Proportion of readmitted for Payer Code = {status}')
    else:
        for i, status in enumerate(payer_code_statuses):
            subset = df_origin[df_origin['payer_code'] == status]
            payer_code_counts = subset['readmitted'].value_counts()
            r = i // ncols
            c = i % ncols
            axes[r, c].pie(payer_code_counts, labels=payer_code_counts.index, autopct='%1.1f%%', startangle=140)
            axes[r, c].set_title(f'Proportion of readmitted for Payer Code = {status}')
    plt.tight_layout()
    st.pyplot(plt)

with tab2:
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df_origin, x='medical_specialty', hue='readmitted', stat="count")
    plt.xlabel('Medical Specialty')
    plt.ylabel("Count")
    plt.title(f'Readmission Status By Medical Specialty')
    plt.xticks(rotation=90)
    plt.tight_layout()
    st.pyplot(plt)

    # medical_specialty_statuses = df_origin['medical_specialty'].dropna().unique()
    # ncols = 4
    # nrows = int(np.ceil(len(medical_specialty_statuses)/ncols))
    # fig,axes=plt.subplots(nrows,ncols,figsize=(8*ncols, 8*nrows))
    # if nrows <= 1:
    #     for i, status in enumerate(medical_specialty_statuses):
    #         subset = df_origin[df_origin['medical_specialty'] == status]
    #         medical_specialty_counts = subset['readmitted'].value_counts()
    #         axes[i].pie(medical_specialty_counts, labels=medical_specialty_counts.index, autopct='%1.1f%%', startangle=140)
    #         axes[i].set_title(f'Proportion of readmitted for Medical Specialty = {status}')
    # else:
    #     for i, status in enumerate(medical_specialty_statuses):
    #         subset = df_origin[df_origin['medical_specialty'] == status]
    #         medical_specialty_counts = subset['readmitted'].value_counts()
    #         r = i // ncols
    #         c = i % ncols
    #         axes[r, c].pie(medical_specialty_counts, labels=medical_specialty_counts.index, autopct='%1.1f%%', startangle=140)
    #         axes[r, c].set_title(f'Proportion of readmitted for Medical Specialty = {status}')
    # plt.tight_layout()
    # st.pyplot(plt)