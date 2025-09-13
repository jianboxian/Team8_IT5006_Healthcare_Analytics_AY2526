import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Healthcare Provider Distribution Histograms")

df_variables = st.session_state["df_variables"]
df_origin = st.session_state["df_origin"]
readmitted_statuses = df_origin['readmitted'].unique()

tab1, tab2 = st.tabs(['max_glu_serum', 'A1Cresult'])

with tab1:
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin, x='max_glu_serum', hue='readmitted', multiple='dodge', shrink=0.8, bins=5)
    plt.title('Max Glucose Serum Count Distribution by Readmission Status')
    plt.xlabel('Max Glucose Serum')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

    max_glu_serum_statuses = df_origin['max_glu_serum'].dropna().unique()
    ncols = 4
    nrows = int(np.ceil(len(max_glu_serum_statuses)/ncols))
    fig,axes=plt.subplots(nrows,ncols,figsize=(8*ncols, 8*nrows))
    if nrows <= 1:
        for i, status in enumerate(max_glu_serum_statuses):
            subset = df_origin[df_origin['max_glu_serum'] == status]
            max_glu_serum_counts = subset['readmitted'].value_counts()
            axes[i].pie(max_glu_serum_counts, labels=max_glu_serum_counts.index, autopct='%1.1f%%', startangle=140)
            axes[i].set_title(f'Proportion of readmitted for Max Glucose Serum = {status}')
    else:
        for i, status in enumerate(max_glu_serum_statuses):
            subset = df_origin[df_origin['max_glu_serum'] == status]
            max_glu_serum_counts = subset['readmitted'].value_counts()
            r = i // ncols
            c = i % ncols
            axes[r, c].pie(max_glu_serum_counts, labels=max_glu_serum_counts.index, autopct='%1.1f%%', startangle=140)
            axes[r, c].set_title(f'Proportion of readmitted for Max Glucose Serum = {status}')
    plt.tight_layout()
    st.pyplot(plt)
with tab2:
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin, x='A1Cresult', hue='readmitted', multiple='dodge', shrink=0.8, bins=5)
    plt.title('A1C Result Count Distribution by Readmission Status')
    plt.xlabel('A1C Result')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)
    A1Cresult_statuses = df_origin['A1Cresult'].dropna().unique()
    ncols = 4
    nrows = int(np.ceil(len(A1Cresult_statuses)/ncols))
    fig,axes=plt.subplots(nrows,ncols,figsize=(8*ncols, 8*nrows))
    if nrows <= 1:
        for i, status in enumerate(A1Cresult_statuses):
            subset = df_origin[df_origin['A1Cresult'] == status]
            A1Cresult_counts = subset['readmitted'].value_counts()
            axes[i].pie(A1Cresult_counts, labels=A1Cresult_counts.index, autopct='%1.1f%%', startangle=140)
            axes[i].set_title(f'Proportion of readmitted for A1C Result = {status}')
    else:
        for i, status in enumerate(A1Cresult_statuses):
            subset = df_origin[df_origin['A1Cresult'] == status]
            A1Cresult_counts = subset['readmitted'].value_counts()
            r = i // ncols
            c = i % ncols
            axes[r, c].pie(A1Cresult_counts, labels=A1Cresult_counts.index, autopct='%1.1f%%', startangle=140)
            axes[r, c].set_title(f'Proportion of readmitted for A1C Result = {status}')
    plt.tight_layout()
    st.pyplot(plt)