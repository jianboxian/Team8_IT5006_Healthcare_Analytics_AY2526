import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Healthcare Provider Distribution Histograms")

df_variables = st.session_state["df_variables"]
df_origin = st.session_state["df_origin"]
readmitted_statuses = df_origin['readmitted'].unique()
tab1, tab2= st.tabs(['change', 'diabetesMed'])

with tab1:
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['change'], bins=5, color='skyblue')
    plt.title('Change Count Distribution')
    plt.xlabel('Change')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)

    change_statuses = df_origin['change'].dropna().unique()
    ncols = 4
    nrows = int(np.ceil(len(change_statuses)/ncols))
    fig,axes=plt.subplots(nrows,ncols,figsize=(8*ncols, 8*nrows))
    if nrows <= 1:
        for i, status in enumerate(change_statuses):
            subset = df_origin[df_origin['change'] == status]
            change_counts = subset['readmitted'].value_counts()
            axes[i].pie(change_counts, labels=change_counts.index, autopct='%1.1f%%', startangle=140)
            axes[i].set_title(f'Proportion of readmitted for Change = {status}')
    else:
        for i, status in enumerate(change_statuses):
            subset = df_origin[df_origin['change'] == status]
            change_counts = subset['readmitted'].value_counts()
            r = i // ncols
            c = i % ncols
            axes[r, c].pie(change_counts, labels=change_counts.index, autopct='%1.1f%%', startangle=140)
            axes[r, c].set_title(f'Proportion of readmitted for Change = {status}')
    plt.tight_layout()
    st.pyplot(plt)
with tab2:
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['diabetesMed'], bins=5, color='lightgreen')
    plt.title('Diabetes Medication Count Distribution')
    plt.xlabel('Diabetes Medication')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)
    diabetesMed_statuses = df_origin['diabetesMed'].dropna().unique()
    ncols = 4
    nrows = int(np.ceil(len(diabetesMed_statuses)/ncols))
    fig,axes=plt.subplots(nrows,ncols,figsize=(8*ncols, 8*nrows))
    if nrows <= 1:
        for i, status in enumerate(diabetesMed_statuses):
            subset = df_origin[df_origin['diabetesMed'] == status]
            diabetesMed_counts = subset['readmitted'].value_counts()
            axes[i].pie(diabetesMed_counts, labels=diabetesMed_counts.index, autopct='%1.1f%%', startangle=140)
            axes[i].set_title(f'Proportion of readmitted for Diabetes Medication = {status}')
    else:
        for i, status in enumerate(diabetesMed_statuses):
            subset = df_origin[df_origin['diabetesMed'] == status]
            diabetesMed_counts = subset['readmitted'].value_counts()
            r = i // ncols
            c = i % ncols
            axes[r, c].pie(diabetesMed_counts, labels=diabetesMed_counts.index, autopct='%1.1f%%', startangle=140)
            axes[r, c].set_title(f'Proportion of readmitted for Diabetes Medication = {status}')
    plt.tight_layout()
    st.pyplot(plt)