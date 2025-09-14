import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Diagnosis Distribution Histograms")

df_variables = st.session_state["df_variables"]
df_origin = st.session_state["df_origin"]
readmitted_statuses = df_origin['readmitted'].unique()

tab1, tab2, tab3= st.tabs(['dia_1', 'diag_2', 'diag_3'])

with tab1:
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='diag_1']['description']}")
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df_origin, x='diag_1', hue='readmitted', stat="count")
    plt.xlabel('Diagnosis 1')
    plt.ylabel("Count")
    plt.title(f'Readmission Status By Diagnosis 1')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

    diagnosis_1_statuses = df_origin['diag_1'].dropna().unique()
    ncols = 4
    nrows = int(np.ceil(len(diagnosis_1_statuses)/ncols))
    fig,axes=plt.subplots(nrows,ncols,figsize=(8*ncols, 8*nrows))
    if nrows <= 1:
        for i, status in enumerate(diagnosis_1_statuses):
            subset = df_origin[df_origin['diag_1'] == status]
            diagnosis_1_counts = subset['readmitted'].value_counts()
            axes[i].pie(diagnosis_1_counts, labels=diagnosis_1_counts.index, autopct='%1.1f%%', startangle=140)
            axes[i].set_title(f'Proportion of readmitted for Diagnosis 1 = {status}')
    else:
        for i, status in enumerate(diagnosis_1_statuses):
            subset = df_origin[df_origin['diag_1'] == status]
            diagnosis_1_counts = subset['readmitted'].value_counts()
            r = i // ncols
            c = i % ncols
            axes[r, c].pie(diagnosis_1_counts, labels=diagnosis_1_counts.index, autopct='%1.1f%%', startangle=140)
            axes[r, c].set_title(f'Proportion of readmitted for Diagnosis 1 = {status}')
    plt.tight_layout()
    st.pyplot(plt)

with tab2:
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='diag_2']['description']}")
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df_origin, x='diag_2', hue='readmitted', stat="count")
    plt.xlabel('Diagnosis 2')
    plt.ylabel("Count")
    plt.title(f'Readmission Status By Diagnosis 2')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

    diagnosis_2_statuses = df_origin['diag_2'].dropna().unique()
    ncols = 4
    nrows = int(np.ceil(len(diagnosis_2_statuses)/ncols))
    fig,axes=plt.subplots(nrows,ncols,figsize=(8*ncols, 8*nrows))
    if nrows <= 1:
        for i, status in enumerate(diagnosis_2_statuses):
            subset = df_origin[df_origin['diag_2'] == status]
            diagnosis_2_counts = subset['readmitted'].value_counts()
            axes[i].pie(diagnosis_2_counts, labels=diagnosis_2_counts.index, autopct='%1.1f%%', startangle=140)
            axes[i].set_title(f'Proportion of readmitted for Diagnosis 2 = {status}')
    else:
        for i, status in enumerate(diagnosis_2_statuses):
            subset = df_origin[df_origin['diag_2'] == status]
            diagnosis_2_counts = subset['readmitted'].value_counts()
            r = i // ncols
            c = i % ncols
            axes[r, c].pie(diagnosis_2_counts, labels=diagnosis_2_counts.index, autopct='%1.1f%%', startangle=140)
            axes[r, c].set_title(f'Proportion of readmitted for Diagnosis 2 = {status}')
    plt.tight_layout()
    st.pyplot(plt)
with tab3:
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='diag_3']['description']}")
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df_origin, x='diag_3', hue='readmitted', stat="count")
    plt.xlabel('Diagnosis 3')
    plt.ylabel("Count")
    plt.title(f'Readmission Status By Diagnosis 3')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

    diagnosis_3_statuses = df_origin['diag_3'].dropna().unique()
    ncols = 4
    nrows = int(np.ceil(len(diagnosis_3_statuses)/ncols))
    fig,axes=plt.subplots(nrows,ncols,figsize=(8*ncols, 8*nrows))
    if nrows <= 1:
        for i, status in enumerate(diagnosis_3_statuses):
            subset = df_origin[df_origin['diag_3'] == status]
            diagnosis_3_counts = subset['readmitted'].value_counts()
            axes[i].pie(diagnosis_3_counts, labels=diagnosis_3_counts.index, autopct='%1.1f%%', startangle=140)
            axes[i].set_title(f'Proportion of readmitted for Diagnosis 3 = {status}')
    else:
        for i, status in enumerate(diagnosis_3_statuses):
            subset = df_origin[df_origin['diag_3'] == status]
            diagnosis_3_counts = subset['readmitted'].value_counts()
            r = i // ncols
            c = i % ncols
            axes[r, c].pie(diagnosis_3_counts, labels=diagnosis_3_counts.index, autopct='%1.1f%%', startangle=140)
            axes[r, c].set_title(f'Proportion of readmitted for Diagnosis 3 = {status}')
    plt.tight_layout()
    st.pyplot(plt)
