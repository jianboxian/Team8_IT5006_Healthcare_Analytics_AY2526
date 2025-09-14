import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Clinical Metrics Distribution Histograms & Pie Chart")

df_variables = st.session_state["df_variables"]
df_origin = st.session_state["df_origin"]
readmitted_statuses = df_origin['readmitted'].unique()

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(['num_lab_procedures', 'num_procedures', 'num_medications','number_outpatient','number_emergency','number_inpatient','number_diagnoses'])
with tab1:
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='num_lab_procedures']['description']}")
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['num_lab_procedures'], color='skyblue', kde=True)
    plt.title(f'Number of Lab Procedures Count Distribution | Skewness: {df_origin["num_lab_procedures"].skew():.2f} | Kurtosis: {df_origin["num_lab_procedures"].kurtosis():.2f}')
    plt.xlabel('Number of Lab Procedures')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)

    # Pie charts for readmitted status within each num_lab_procedures category
    num_lab_procedures_statuses = df_origin['num_lab_procedures'].dropna().unique()
    ncols = 4
    nrows = int(np.ceil(len(num_lab_procedures_statuses)/ncols))
    fig,axes=plt.subplots(nrows,ncols,figsize=(8*ncols, 8*nrows))
    if nrows == 1:
        for i, status in enumerate(num_lab_procedures_statuses):
            subset = df_origin[df_origin['num_lab_procedures'] == status]
            lab_counts = subset['readmitted'].value_counts()
            axes[i].pie(lab_counts, labels=lab_counts.index, autopct='%1.1f%%', startangle=140)
            axes[i].set_title(f'Proportion of readmitted for Num Lab Procedures = {status}')
        for j in range(i+1, len(axes)):
            fig.delaxes(axes[j])
    else:
        for i, status in enumerate(num_lab_procedures_statuses):
            subset = df_origin[df_origin['num_lab_procedures'] == status]
            lab_counts = subset['readmitted'].value_counts()
            r = i // ncols
            c = i % ncols
            axes[r, c].pie(lab_counts, labels=lab_counts.index, autopct='%1.1f%%', startangle=140)
            axes[r, c].set_title(f'Proportion of readmitted for Num Lab Procedures = {status}')
        for j in range(i+1, len(axes.flatten())):
            fig.delaxes(axes.flatten()[j])
    plt.tight_layout()
    st.pyplot(plt)
with tab2:
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='num_procedures']['description']}")
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['num_procedures'], color='skyblue', kde=True)
    plt.title(f'Number of Procedures Count Distribution | Skewness: {df_origin["num_procedures"].skew():.2f} | Kurtosis: {df_origin["num_procedures"].kurtosis():.2f}')
    plt.xlabel('Number of Procedures')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)

    num_procedures_statuses = df_origin['num_procedures'].dropna().unique()
    ncols = 4
    nrows = int(np.ceil(len(num_procedures_statuses)/ncols))
    fig,axes=plt.subplots(nrows,ncols,figsize=(8*ncols, 8*nrows))
    if nrows == 1:
        for i, status in enumerate(num_procedures_statuses):
            subset = df_origin[df_origin['num_procedures'] == status]
            procedure_counts = subset['readmitted'].value_counts()
            axes[i].pie(procedure_counts, labels=procedure_counts.index, autopct='%1.1f%%', startangle=140)
            axes[i].set_title(f'Proportion of readmitted for Num Procedures = {status}')
        for j in range(i+1, len(axes)):
            fig.delaxes(axes[j])
    else:
        for i, status in enumerate(num_procedures_statuses):
            subset = df_origin[df_origin['num_procedures'] == status]
            procedure_counts = subset['readmitted'].value_counts()
            r = i // ncols
            c = i % ncols
            axes[r, c].pie(procedure_counts, labels=procedure_counts.index, autopct='%1.1f%%', startangle=140)
            axes[r, c].set_title(f'Proportion of readmitted for Num Procedures = {status}')
        for j in range(i+1, len(axes.flatten())):
            fig.delaxes(axes.flatten()[j])
    plt.tight_layout()
    st.pyplot(plt)
with tab3:
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='num_medications']['description']}")
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['num_medications'], color='skyblue', kde=True)
    plt.title(f'Number of Medications Count Distribution | Skewness: {df_origin["num_medications"].skew():.2f} | Kurtosis: {df_origin["num_medications"].kurtosis():.2f}')
    plt.xlabel('Number of Medications')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)

    num_medications_statuses = df_origin['num_medications'].dropna().unique()
    ncols = 4
    nrows = int(np.ceil(len(num_medications_statuses)/ncols))
    fig,axes=plt.subplots(nrows,ncols,figsize=(8*ncols, 8*nrows))
    if nrows == 1:
        for i, status in enumerate(num_medications_statuses):
            subset = df_origin[df_origin['num_medications'] == status]
            medication_counts = subset['readmitted'].value_counts()
            axes[i].pie(medication_counts, labels=medication_counts.index, autopct='%1.1f%%', startangle=140)
            axes[i].set_title(f'Proportion of readmitted for Num Medications = {status}')
        for j in range(i+1, len(axes)):
            fig.delaxes(axes[j])
    else:
        for i, status in enumerate(num_medications_statuses):
            subset = df_origin[df_origin['num_medications'] == status]
            medication_counts = subset['readmitted'].value_counts()
            r = i // ncols
            c = i % ncols
            axes[r, c].pie(medication_counts, labels=medication_counts.index, autopct='%1.1f%%', startangle=140)
            axes[r, c].set_title(f'Proportion of readmitted for Num Medications = {status}')
        for j in range(i+1, len(axes.flatten())):
            fig.delaxes(axes.flatten()[j])
    plt.tight_layout()
    st.pyplot(plt)
with tab4:
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='number_outpatient']['description']}")
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['number_outpatient'], color='skyblue', kde=True)
    plt.title(f'Number of Outpatient Count Distribution | Skewness: {df_origin["number_outpatient"].skew():.2f} | Kurtosis: {df_origin["number_outpatient"].kurtosis():.2f}')
    plt.xlabel('Number of Outpatient')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)

    number_outpatient_statuses = df_origin['number_outpatient'].dropna().unique()
    ncols = 4
    nrows = int(np.ceil(len(number_outpatient_statuses)/ncols))
    fig,axes=plt.subplots(nrows,ncols,figsize=(8*ncols, 8*nrows))
    if nrows == 1:
        for i, status in enumerate(number_outpatient_statuses):
            subset = df_origin[df_origin['number_outpatient'] == status]
            outpatient_counts = subset['readmitted'].value_counts()
            axes[i].pie(outpatient_counts, labels=outpatient_counts.index, autopct='%1.1f%%', startangle=140)
            axes[i].set_title(f'Proportion of readmitted for Number Outpatient = {status}')
        for j in range(i+1, len(axes)):
            fig.delaxes(axes[j])
    else:
        for i, status in enumerate(number_outpatient_statuses):
            subset = df_origin[df_origin['number_outpatient'] == status]
            outpatient_counts = subset['readmitted'].value_counts()
            r = i // ncols
            c = i % ncols
            axes[r, c].pie(outpatient_counts, labels=outpatient_counts.index, autopct='%1.1f%%', startangle=140)
            axes[r, c].set_title(f'Proportion of readmitted for Number Outpatient = {status}')
        for j in range(i+1, len(axes.flatten())):
            fig.delaxes(axes.flatten()[j])
    plt.tight_layout()
    st.pyplot(plt)
with tab5:
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='number_emergency']['description']}")
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['number_emergency'], color='skyblue', kde=True)
    plt.title(f'Number of Emergency Count Distribution | Skewness: {df_origin["number_emergency"].skew():.2f} | Kurtosis: {df_origin["number_emergency"].kurtosis():.2f}')
    plt.xlabel('Number of Emergency')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)

    number_emergency_statuses = df_origin['number_emergency'].dropna().unique()
    ncols = 4
    nrows = int(np.ceil(len(number_emergency_statuses)/ncols))
    fig,axes=plt.subplots(nrows,ncols,figsize=(8*ncols, 8*nrows))
    if nrows == 1:
        for i, status in enumerate(number_emergency_statuses):
            subset = df_origin[df_origin['number_emergency'] == status]
            emergency_counts = subset['readmitted'].value_counts()
            axes[i].pie(emergency_counts, labels=emergency_counts.index, autopct='%1.1f%%', startangle=140)
            axes[i].set_title(f'Proportion of readmitted for Number Emergency = {status}')
        for j in range(i+1, len(axes)):
            fig.delaxes(axes[j])
    else:
        for i, status in enumerate(number_emergency_statuses):
            subset = df_origin[df_origin['number_emergency'] == status]
            emergency_counts = subset['readmitted'].value_counts()
            r = i // ncols
            c = i % ncols
            axes[r, c].pie(emergency_counts, labels=emergency_counts.index, autopct='%1.1f%%', startangle=140)
            axes[r, c].set_title(f'Proportion of readmitted for Number Emergency = {status}')
        for j in range(i+1, len(axes.flatten())):
            fig.delaxes(axes.flatten()[j])
    plt.tight_layout()
    st.pyplot(plt)
with tab6:
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='number_inpatient']['description']}")
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['number_inpatient'], color='skyblue', kde=True)
    plt.title(f'Number of Inpatient Count Distribution | Skewness: {df_origin["number_inpatient"].skew():.2f} | Kurtosis: {df_origin["number_inpatient"].kurtosis():.2f}')
    plt.xlabel('Number of Inpatient')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)

    number_inpatient_statuses = df_origin['number_inpatient'].dropna().unique()
    ncols = 4
    nrows = int(np.ceil(len(number_inpatient_statuses)/ncols))
    fig,axes=plt.subplots(nrows,ncols,figsize=(8*ncols, 8*nrows))
    if nrows == 1:
        for i, status in enumerate(number_inpatient_statuses):
            subset = df_origin[df_origin['number_inpatient'] == status]
            inpatient_counts = subset['readmitted'].value_counts()
            axes[i].pie(inpatient_counts, labels=inpatient_counts.index, autopct='%1.1f%%', startangle=140)
            axes[i].set_title(f'Proportion of readmitted for Number Inpatient = {status}')
        for j in range(i+1, len(axes)):
            fig.delaxes(axes[j])
    else:
        for i, status in enumerate(number_inpatient_statuses):
            subset = df_origin[df_origin['number_inpatient'] == status]
            inpatient_counts = subset['readmitted'].value_counts()
            r = i // ncols
            c = i % ncols
            axes[r, c].pie(inpatient_counts, labels=inpatient_counts.index, autopct='%1.1f%%', startangle=140)
            axes[r, c].set_title(f'Proportion of readmitted for Number Inpatient = {status}')
        for j in range(i+1, len(axes.flatten())):
            fig.delaxes(axes.flatten()[j])
    plt.tight_layout()
    st.pyplot(plt)
with tab7:
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='number_diagnoses']['description']}")
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['number_diagnoses'], color='skyblue', kde=True)
    plt.title(f'Number of Diagnoses Count Distribution | Skewness: {df_origin["number_diagnoses"].skew():.2f} | Kurtosis: {df_origin["number_diagnoses"].kurtosis():.2f}')
    plt.xlabel('Number of Diagnoses')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)

    number_diagnoses_statuses = df_origin['number_diagnoses'].dropna().unique()
    ncols = 4
    nrows = int(np.ceil(len(number_diagnoses_statuses)/ncols))
    fig,axes=plt.subplots(nrows,ncols,figsize=(8*ncols, 8*nrows))
    if nrows == 1:
        for i, status in enumerate(number_diagnoses_statuses):
            subset = df_origin[df_origin['number_diagnoses'] == status]
            diagnoses_counts = subset['readmitted'].value_counts()
            axes[i].pie(diagnoses_counts, labels=diagnoses_counts.index, autopct='%1.1f%%', startangle=140)
            axes[i].set_title(f'Proportion of readmitted for Number Diagnoses = {status}')
        for j in range(i+1, len(axes)):
            fig.delaxes(axes[j])
    else:
        for i, status in enumerate(number_diagnoses_statuses):
            subset = df_origin[df_origin['number_diagnoses'] == status]
            diagnoses_counts = subset['readmitted'].value_counts()
            r = i // ncols
            c = i % ncols
            axes[r, c].pie(diagnoses_counts, labels=diagnoses_counts.index, autopct='%1.1f%%', startangle=140)
            axes[r, c].set_title(f'Proportion of readmitted for Number Diagnoses = {status}')
        for j in range(i+1, len(axes.flatten())):
            fig.delaxes(axes.flatten()[j])
    plt.tight_layout()
    st.pyplot(plt)