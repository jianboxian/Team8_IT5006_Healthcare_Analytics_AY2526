import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Medications Distribution Histograms & Pie Chart")

df_variables = st.session_state["df_variables"]
df_origin = st.session_state["df_origin"]
readmitted_statuses = df_origin['readmitted'].unique()
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(['metformin', 'repaglinide','nateglinide','chlorpropamide','glimepiride','glipizide','glyburide','pioglitazone','rosiglitazone','insulin'])
with tab1:
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='metformin']['description']}")
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['metformin'], bins=5, color='skyblue')
    plt.title('Metformin Count Distribution')
    plt.xlabel('Metformin')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)

    metformin_statuses = df_origin['metformin'].dropna().unique()
    ncols = 4
    nrows = int(np.ceil(len(metformin_statuses)/ncols))
    fig,axes=plt.subplots(nrows,ncols,figsize=(8*ncols, 8*nrows))
    if nrows <= 1:
        for i, status in enumerate(metformin_statuses):
            subset = df_origin[df_origin['metformin'] == status]
            metformin_counts = subset['readmitted'].value_counts()
            axes[i].pie(metformin_counts, labels=metformin_counts.index, autopct='%1.1f%%', startangle=140)
            axes[i].set_title(f'Proportion of readmitted for Metformin = {status}')
    else:
        for i, status in enumerate(metformin_statuses):
            subset = df_origin[df_origin['metformin'] == status]
            metformin_counts = subset['readmitted'].value_counts()
            r = i // ncols
            c = i % ncols
            axes[r, c].pie(metformin_counts, labels=metformin_counts.index, autopct='%1.1f%%', startangle=140)
            axes[r, c].set_title(f'Proportion of readmitted for Metformin = {status}')
    plt.tight_layout()
    st.pyplot(plt)
with tab2:
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='repaglinide']['description']}")
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['repaglinide'], bins=5, color='lightgreen')
    plt.title('Repaglinide Count Distribution')
    plt.xlabel('Repaglinide')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)
    repaglinide_statuses = df_origin['repaglinide'].dropna().unique()
    ncols = 4
    nrows = int(np.ceil(len(repaglinide_statuses)/ncols))
    fig,axes=plt.subplots(nrows,ncols,figsize=(8*ncols, 8*nrows))
    if nrows <= 1:
        for i, status in enumerate(repaglinide_statuses):
            subset = df_origin[df_origin['repaglinide'] == status]
            repaglinide_counts = subset['readmitted'].value_counts()
            axes[i].pie(repaglinide_counts, labels=repaglinide_counts.index, autopct='%1.1f%%', startangle=140)
            axes[i].set_title(f'Proportion of readmitted for Repaglinide = {status}')
    else:
        for i, status in enumerate(repaglinide_statuses):
            subset = df_origin[df_origin['repaglinide'] == status]
            repaglinide_counts = subset['readmitted'].value_counts()
            r = i // ncols
            c = i % ncols
            axes[r, c].pie(repaglinide_counts, labels=repaglinide_counts.index, autopct='%1.1f%%', startangle=140)
            axes[r, c].set_title(f'Proportion of readmitted for Repaglinide = {status}')
    plt.tight_layout()
    st.pyplot(plt)
with tab3:
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='nateglinide']['description']}")
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['nateglinide'], bins=5, color='salmon')
    plt.title('Nateglinide Count Distribution')
    plt.xlabel('Nateglinide')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)
    nateglinide_statuses = df_origin['nateglinide'].dropna().unique()
    ncols = 4
    nrows = int(np.ceil(len(nateglinide_statuses)/ncols))
    fig,axes=plt.subplots(nrows,ncols,figsize=(8*ncols, 8*nrows))
    if nrows <= 1:
        for i, status in enumerate(nateglinide_statuses):
            subset = df_origin[df_origin['nateglinide'] == status]
            nateglinide_counts = subset['readmitted'].value_counts()
            axes[i].pie(nateglinide_counts, labels=nateglinide_counts.index, autopct='%1.1f%%', startangle=140)
            axes[i].set_title(f'Proportion of readmitted for Nateglinide = {status}')
    else:
        for i, status in enumerate(nateglinide_statuses):
            subset = df_origin[df_origin['nateglinide'] == status]
            nateglinide_counts = subset['readmitted'].value_counts()
            r = i // ncols
            c = i % ncols
            axes[r, c].pie(nateglinide_counts, labels=nateglinide_counts.index, autopct='%1.1f%%', startangle=140)
            axes[r, c].set_title(f'Proportion of readmitted for Nateglinide = {status}')
    plt.tight_layout()
    st.pyplot(plt)
with tab4:
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='chlorpropamide']['description']}")
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['chlorpropamide'], bins=5, color='violet')
    plt.title('Chlorpropamide Count Distribution')
    plt.xlabel('Chlorpropamide')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)
    chlorpropamide_statuses = df_origin['chlorpropamide'].dropna().unique()
    ncols = 4
    nrows = int(np.ceil(len(chlorpropamide_statuses)/ncols))
    fig,axes=plt.subplots(nrows,ncols,figsize=(8*ncols, 8*nrows))
    if nrows <= 1:
        for i, status in enumerate(chlorpropamide_statuses):
            subset = df_origin[df_origin['chlorpropamide'] == status]
            chlorpropamide_counts = subset['readmitted'].value_counts()
            axes[i].pie(chlorpropamide_counts, labels=chlorpropamide_counts.index, autopct='%1.1f%%', startangle=140)
            axes[i].set_title(f'Proportion of readmitted for Chlorpropamide = {status}')
    else:
        for i, status in enumerate(chlorpropamide_statuses):
            subset = df_origin[df_origin['chlorpropamide'] == status]
            chlorpropamide_counts = subset['readmitted'].value_counts()
            r = i // ncols
            c = i % ncols
            axes[r, c].pie(chlorpropamide_counts, labels=chlorpropamide_counts.index, autopct='%1.1f%%', startangle=140)
            axes[r, c].set_title(f'Proportion of readmitted for Chlorpropamide = {status}')
    plt.tight_layout()
    st.pyplot(plt)
with tab5:
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='glimepiride']['description']}")
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['glimepiride'], bins=5, color='orange')
    plt.title('Glimepiride Count Distribution')
    plt.xlabel('Glimepiride')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)
    glimepiride_statuses = df_origin['glimepiride'].dropna().unique()
    ncols = 4
    nrows = int(np.ceil(len(glimepiride_statuses)/ncols))
    fig,axes=plt.subplots(nrows,ncols,figsize=(8*ncols, 8*nrows))
    if nrows <= 1:
        for i, status in enumerate(glimepiride_statuses):
            subset = df_origin[df_origin['glimepiride'] == status]
            glimepiride_counts = subset['readmitted'].value_counts()
            axes[i].pie(glimepiride_counts, labels=glimepiride_counts.index, autopct='%1.1f%%', startangle=140)
            axes[i].set_title(f'Proportion of readmitted for Glimepiride = {status}')
    else:
        for i, status in enumerate(glimepiride_statuses):
            subset = df_origin[df_origin['glimepiride'] == status]
            glimepiride_counts = subset['readmitted'].value_counts()
            r = i // ncols
            c = i % ncols
            axes[r, c].pie(glimepiride_counts, labels=glimepiride_counts.index, autopct='%1.1f%%', startangle=140)
            axes[r, c].set_title(f'Proportion of readmitted for Glimepiride = {status}')
    plt.tight_layout()
    st.pyplot(plt)
with tab6:
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='glipizide']['description']}")
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['glipizide'], bins=5, color='lightblue')
    plt.title('Glipizide Count Distribution')
    plt.xlabel('Glipizide')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)
    glipizide_statuses = df_origin['glipizide'].dropna().unique()
    ncols = 4
    nrows = int(np.ceil(len(glipizide_statuses)/ncols))
    fig,axes=plt.subplots(nrows,ncols,figsize=(8*ncols, 8*nrows))
    if nrows <= 1:
        for i, status in enumerate(glipizide_statuses):
            subset = df_origin[df_origin['glipizide'] == status]
            glipizide_counts = subset['readmitted'].value_counts()
            axes[i].pie(glipizide_counts, labels=glipizide_counts.index, autopct='%1.1f%%', startangle=140)
            axes[i].set_title(f'Proportion of readmitted for Glipizide = {status}')
    else:
        for i, status in enumerate(glipizide_statuses):
            subset = df_origin[df_origin['glipizide'] == status]
            glipizide_counts = subset['readmitted'].value_counts()
            r = i // ncols
            c = i % ncols
            axes[r, c].pie(glipizide_counts, labels=glipizide_counts.index, autopct='%1.1f%%', startangle=140)
            axes[r, c].set_title(f'Proportion of readmitted for Glipizide = {status}')
    plt.tight_layout()
    st.pyplot(plt)
with tab7:
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='glyburide']['description']}")
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['glyburide'], bins=5, color='lightcoral')
    plt.title('Glyburide Count Distribution')
    plt.xlabel('Glyburide')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)
    glyburide_statuses = df_origin['glyburide'].dropna().unique()
    ncols = 4
    nrows = int(np.ceil(len(glyburide_statuses)/ncols))
    fig,axes=plt.subplots(nrows,ncols,figsize=(8*ncols, 8*nrows))
    if nrows <= 1:
        for i, status in enumerate(glyburide_statuses):
            subset = df_origin[df_origin['glyburide'] == status]
            glyburide_counts = subset['readmitted'].value_counts()
            axes[i].pie(glyburide_counts, labels=glyburide_counts.index, autopct='%1.1f%%', startangle=140)
            axes[i].set_title(f'Proportion of readmitted for Glyburide = {status}')
    else:
        for i, status in enumerate(glyburide_statuses):
            subset = df_origin[df_origin['glyburide'] == status]
            glyburide_counts = subset['readmitted'].value_counts()
            r = i // ncols
            c = i % ncols
            axes[r, c].pie(glyburide_counts, labels=glyburide_counts.index, autopct='%1.1f%%', startangle=140)
            axes[r, c].set_title(f'Proportion of readmitted for Glyburide = {status}')
    plt.tight_layout()
    st.pyplot(plt)
with tab8:
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='pioglitazone']['description']}")
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['pioglitazone'], bins=5, color='lightseagreen')
    plt.title('Pioglitazone Count Distribution')
    plt.xlabel('Pioglitazone')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)
    pioglitazone_statuses = df_origin['pioglitazone'].dropna().unique()
    ncols = 4
    nrows = int(np.ceil(len(pioglitazone_statuses)/ncols))
    fig,axes=plt.subplots(nrows,ncols,figsize=(8*ncols, 8*nrows))
    if nrows <= 1:
        for i, status in enumerate(pioglitazone_statuses):
            subset = df_origin[df_origin['pioglitazone'] == status]
            pioglitazone_counts = subset['readmitted'].value_counts()
            axes[i].pie(pioglitazone_counts, labels=pioglitazone_counts.index, autopct='%1.1f%%', startangle=140)
            axes[i].set_title(f'Proportion of readmitted for Pioglitazone = {status}')
    else:
        for i, status in enumerate(pioglitazone_statuses):
            subset = df_origin[df_origin['pioglitazone'] == status]
            pioglitazone_counts = subset['readmitted'].value_counts()
            r = i // ncols
            c = i % ncols
            axes[r, c].pie(pioglitazone_counts, labels=pioglitazone_counts.index, autopct='%1.1f%%', startangle=140)
            axes[r, c].set_title(f'Proportion of readmitted for Pioglitazone = {status}')
    plt.tight_layout()
    st.pyplot(plt)
with tab9:
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='rosiglitazone']['description']}")
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['rosiglitazone'], bins=5, color='plum')
    plt.title('Rosiglitazone Count Distribution')
    plt.xlabel('Rosiglitazone')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)
    rosiglitazone_statuses = df_origin['rosiglitazone'].dropna().unique()
    ncols = 4
    nrows = int(np.ceil(len(rosiglitazone_statuses)/ncols))
    fig,axes=plt.subplots(nrows,ncols,figsize=(8*ncols, 8*nrows))
    if nrows <= 1:
        for i, status in enumerate(rosiglitazone_statuses):
            subset = df_origin[df_origin['rosiglitazone'] == status]
            rosiglitazone_counts = subset['readmitted'].value_counts()
            axes[i].pie(rosiglitazone_counts, labels=rosiglitazone_counts.index, autopct='%1.1f%%', startangle=140)
            axes[i].set_title(f'Proportion of readmitted for Rosiglitazone = {status}')
    else:
        for i, status in enumerate(rosiglitazone_statuses):
            subset = df_origin[df_origin['rosiglitazone'] == status]
            rosiglitazone_counts = subset['readmitted'].value_counts()
            r = i // ncols
            c = i % ncols
            axes[r, c].pie(rosiglitazone_counts, labels=rosiglitazone_counts.index, autopct='%1.1f%%', startangle=140)
            axes[r, c].set_title(f'Proportion of readmitted for Rosiglitazone = {status}')
    plt.tight_layout()
    st.pyplot(plt)
with tab10:
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='insulin']['description']}")
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_origin['insulin'], bins=5, color='lightpink')
    plt.title('Insulin Count Distribution')
    plt.xlabel('Insulin')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)
    insulin_statuses = df_origin['insulin'].dropna().unique()
    ncols = 4
    nrows = int(np.ceil(len(insulin_statuses)/ncols))
    fig,axes=plt.subplots(nrows,ncols,figsize=(8*ncols, 8*nrows))
    if nrows <= 1:
        for i, status in enumerate(insulin_statuses):
            subset = df_origin[df_origin['insulin'] == status]
            insulin_counts = subset['readmitted'].value_counts()
            axes[i].pie(insulin_counts, labels=insulin_counts.index, autopct='%1.1f%%', startangle=140)
            axes[i].set_title(f'Proportion of readmitted for Insulin = {status}')
    else:
        for i, status in enumerate(insulin_statuses):
            subset = df_origin[df_origin['insulin'] == status]
            insulin_counts = subset['readmitted'].value_counts()
            r = i // ncols
            c = i % ncols
            axes[r, c].pie(insulin_counts, labels=insulin_counts.index, autopct='%1.1f%%', startangle=140)
            axes[r, c].set_title(f'Proportion of readmitted for Insulin = {status}')
    plt.tight_layout()
    st.pyplot(plt)

