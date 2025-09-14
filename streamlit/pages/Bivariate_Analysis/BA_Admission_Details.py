import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Admission Details Distribution Histograms & Pie Chart & BoxPlot")

df_variables = st.session_state["df_variables"]
df_origin = st.session_state["df_origin"]
readmitted_statuses = df_origin['readmitted'].unique()


tab1, tab2, tab3, tab4, tab5 = st.tabs(['admission_type_id', 'discharge_disposition_id', 'admission_source_id','time_in_hospital','time_in_hospital BoxPlot'])

with tab1:
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='admission_type_id']['description']}")
    st.markdown(""" **Type of admission** : `1`:Emergency  `2`:Urgent  `3`:Elective  etc.""")
    st.markdown(""" **Findings and Observations**:  
- Preliminary observations show that emergency-related admissions dominate the dataset, with over 50,000 patient encounters marked as either emergency-type. This reflects the real-world clinical severity of diabetes exacerbations requiring urgent intervention. """)
    st.markdown("---")
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
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='discharge_disposition_id']['description']}")
    st.markdown(""" **Discharge destination** : `1`:Home  `3`:SNF  `6`:Home with service  etc.""")
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
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='admission_source_id']['description']}")
    st.markdown(""" **Source of admission** : `1`:Physician referral `7`:Emergency room  etc.""")
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
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='time_in_hospital']['description']}")
    st.markdown(""" **Number of days in hospital (1-14 days)** """)
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

with tab5:
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='time_in_hospital']['description']}")
    st.markdown(""" **Number of days in hospital (1-14 days)** """)
    st.markdown(""" **Findings and Observations**:  
- Time in Hospital: Although the interquartile range at 25th-75th percentile appears similar across different patient groups, we observe that the median hospital stay duration was longer for patients who were readmitted (both early and late) """)
    st.markdown("---")
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='readmitted', y='time_in_hospital', data=df_origin)
    plt.title(f'Time in Hospital Distribution by Readmission Status BoxPlot')
    plt.ylabel('Time in Hospital')
    plt.xlabel('Readmission Status')
    plt.tight_layout()
    st.pyplot(plt)