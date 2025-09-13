import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Admission Details Distribution Histograms")

df_variables = st.session_state["df_variables"]
df_origin = st.session_state["df_origin"]
readmitted_statuses = df_origin['readmitted'].unique()


tab1, tab2, tab3, tab4 = st.tabs(['admission_type_id', 'discharge_disposition_id', 'admission_source_id','time_in_hospital'])

with tab1:
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df_origin, x='admission_type_id', hue='readmitted', stat="count")
    plt.xlabel('Admission Type ID')
    plt.ylabel("Count")
    plt.title(f'Readmission Status By Admission Type ID')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

    admission_type_statuses = df_origin['admission_type_id'].dropna().unique()
    ncols = 4
    nrows = int(np.ceil(len(admission_type_statuses)/ncols))
    fig,axes=plt.subplots(nrows,ncols,figsize=(8*ncols, 8*nrows))
    if nrows <= 1:
        for i, status in enumerate(admission_type_statuses):
            subset = df_origin[df_origin['admission_type_id'] == status]
            admission_type_counts = subset['readmitted'].value_counts()
            axes[i].pie(admission_type_counts, labels=admission_type_counts.index, autopct='%1.1f%%', startangle=140)
            axes[i].set_title(f'Proportion of readmitted for Admission Type ID = {status}')
    else:
        for i, status in enumerate(admission_type_statuses):
            subset = df_origin[df_origin['admission_type_id'] == status]
            admission_type_counts = subset['readmitted'].value_counts()
            r = i // ncols
            c = i % ncols
            axes[r, c].pie(admission_type_counts, labels=admission_type_counts.index, autopct='%1.1f%%', startangle=140)
            axes[r, c].set_title(f'Proportion of readmitted for Admission Type ID = {status}')
    plt.tight_layout()
    st.pyplot(plt)
with tab2:
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df_origin, x='discharge_disposition_id', hue='readmitted', stat="count")
    plt.xlabel('Discharge Disposition ID')
    plt.ylabel("Count")
    plt.title(f'Readmission Status By Discharge Disposition ID')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

    discharge_disposition_statuses = df_origin['discharge_disposition_id'].dropna().unique()
    ncols = 4
    nrows = int(np.ceil(len(discharge_disposition_statuses)/ncols))
    fig,axes=plt.subplots(nrows,ncols,figsize=(8*ncols, 8*nrows))
    if nrows <= 1:
        for i, status in enumerate(discharge_disposition_statuses):
            subset = df_origin[df_origin['discharge_disposition_id'] == status]
            discharge_disposition_counts = subset['readmitted'].value_counts()
            axes[i].pie(discharge_disposition_counts, labels=discharge_disposition_counts.index, autopct='%1.1f%%', startangle=140)
            axes[i].set_title(f'Proportion of readmitted for Discharge Disposition ID = {status}')
    else:
        for i, status in enumerate(discharge_disposition_statuses):
            subset = df_origin[df_origin['discharge_disposition_id'] == status]
            discharge_disposition_counts = subset['readmitted'].value_counts()
            r = i // ncols
            c = i % ncols
            axes[r, c].pie(discharge_disposition_counts, labels=discharge_disposition_counts.index, autopct='%1.1f%%', startangle=140)
            axes[r, c].set_title(f'Proportion of readmitted for Discharge Disposition ID = {status}')
    plt.tight_layout()
    st.pyplot(plt)
with tab3:
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df_origin, x='admission_source_id', hue='readmitted', stat="count")
    plt.xlabel('Admission Source ID')
    plt.ylabel("Count")
    plt.title(f'Readmission Status By Admission Source ID')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)
    
    admission_source_statuses = df_origin['admission_source_id'].dropna().unique()
    ncols = 4
    nrows = int(np.ceil(len(admission_source_statuses)/ncols))
    fig,axes=plt.subplots(nrows,ncols,figsize=(8*ncols, 8*nrows))
    if nrows <= 1:
        for i, status in enumerate(admission_source_statuses):
            subset = df_origin[df_origin['admission_source_id'] == status]
            admission_source_counts = subset['readmitted'].value_counts()
            axes[i].pie(admission_source_counts, labels=admission_source_counts.index, autopct='%1.1f%%', startangle=140)
            axes[i].set_title(f'Proportion of readmitted for Admission Source ID = {status}')
    else:
        for i, status in enumerate(admission_source_statuses):
            subset = df_origin[df_origin['admission_source_id'] == status]
            admission_source_counts = subset['readmitted'].value_counts()
            r = i // ncols
            c = i % ncols
            axes[r, c].pie(admission_source_counts, labels=admission_source_counts.index, autopct='%1.1f%%', startangle=140)
            axes[r, c].set_title(f'Proportion of readmitted for Admission Source ID = {status}')
    plt.tight_layout()
    st.pyplot(plt)

with tab4:
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df_origin, x='time_in_hospital', hue='readmitted', stat="count")
    plt.xlabel('Time in Hospital')
    plt.ylabel("Count")
    plt.title(f'Readmission Status By Time in Hospital')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

    time_in_hospital_statuses = df_origin['time_in_hospital'].dropna().unique()
    ncols = 4
    nrows = int(np.ceil(len(time_in_hospital_statuses)/ncols))
    fig,axes=plt.subplots(nrows,ncols,figsize=(8*ncols, 8*nrows))
    if nrows <= 1:
        for i, status in enumerate(time_in_hospital_statuses):
            subset = df_origin[df_origin['time_in_hospital'] == status]
            time_in_hospital_counts = subset['readmitted'].value_counts()
            axes[i].pie(time_in_hospital_counts, labels=time_in_hospital_counts.index, autopct='%1.1f%%', startangle=140)
            axes[i].set_title(f'Proportion of readmitted for Time in Hospital = {status}')
    else:
        for i, status in enumerate(time_in_hospital_statuses):
            subset = df_origin[df_origin['time_in_hospital'] == status]
            time_in_hospital_counts = subset['readmitted'].value_counts()
            r = i // ncols
            c = i % ncols
            axes[r, c].pie(time_in_hospital_counts, labels=time_in_hospital_counts.index, autopct='%1.1f%%', startangle=140)
            axes[r, c].set_title(f'Proportion of readmitted for Time in Hospital = {status}')
    plt.tight_layout()
    st.pyplot(plt)