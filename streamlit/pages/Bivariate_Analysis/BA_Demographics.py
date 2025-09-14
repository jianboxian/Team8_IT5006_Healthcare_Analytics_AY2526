import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Demographic Distribution Histograms & Pie Chart")

df_variables = st.session_state["df_variables"]
df_origin = st.session_state["df_origin"]
readmitted_statuses = df_origin['readmitted'].unique()


tab1, tab2, tab3, tab4 = st.tabs(['Age', 'Gender', 'Race','Weight'])


with tab1:
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='age']['description']}")
    st.markdown(""" **Findings and Observations**:  
- There is a general trend of higher numbers of patients in older age brackets. Patients aged [70-80] form the largest group, followed by those aged [60-70] and [50-60]. However, patients aged [20-30] exhibited an early readmission rate of 14.2% , which is significantly higher than the average for older groups with around 10-11%.  """)
    st.markdown("---")
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df_origin, x='age', hue='readmitted', stat="count")
    plt.xlabel('Age')
    plt.ylabel("Count")
    plt.title(f'Readmission Status By Age')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

    age_statuses = df_origin['age'].dropna().unique()
    ncols = 4
    nrows = int(np.ceil(len(age_statuses)/ncols))
    fig,axes=plt.subplots(nrows,ncols,figsize=(8*ncols, 8*nrows))
    if nrows <= 1:
        for i, status in enumerate(age_statuses):
            subset = df_origin[df_origin['age'] == status]
            age_counts = subset['readmitted'].value_counts()
            axes[i].pie(age_counts, labels=age_counts.index, autopct='%1.1f%%', startangle=140)
            axes[i].set_title(f'Proportion of readmitted for Age = {status}')
    else:
        for i, status in enumerate(age_statuses):
            subset = df_origin[df_origin['age'] == status]
            age_counts = subset['readmitted'].value_counts()
            r = i // ncols
            c = i % ncols
            axes[r, c].pie(age_counts, labels=age_counts.index, autopct='%1.1f%%', startangle=140)
            axes[r, c].set_title(f'Proportion of readmitted for Age = {status}')
    plt.tight_layout()
    st.pyplot(plt)

with tab2:
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='gender']['description']}")
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df_origin, x='gender', hue='readmitted', stat="count")
    plt.xlabel('Gender')
    plt.ylabel("Count")
    plt.title(f'Readmission Status By Gender')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)
    gender_statuses = df_origin['gender'].dropna().unique()
    ncols = 4
    nrows = int(np.ceil(len(gender_statuses)/ncols))
    fig,axes=plt.subplots(nrows,ncols,figsize=(8*ncols, 8*nrows))
    if nrows <= 1:
        for i, status in enumerate(gender_statuses):
            subset = df_origin[df_origin['gender'] == status]
            gender_counts = subset['readmitted'].value_counts()
            axes[i].pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140)
            axes[i].set_title(f'Proportion of readmitted for Gender = {status}')
    else:
        for i, status in enumerate(gender_statuses):
            subset = df_origin[df_origin['gender'] == status]
            gender_counts = subset['readmitted'].value_counts()
            r = i // ncols
            c = i % ncols
            axes[r, c].pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140)
            axes[r, c].set_title(f'Proportion of readmitted for Gender = {status}')
    plt.tight_layout()
    st.pyplot(plt)

with tab3:
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='race']['description']}")
    st.markdown(""" **Findings and Observations**:  
- The sample dataset contains a significant racial imbalance, as over 70,000 patients are caucasian, followed by approximately 20,000 African American. While the remaining racial groups, Hispanic, Asian and Others, each represent less than 10,000 patient cases. Despite this disparity, the proportion of patients readmitted early is relatively consistent across races at around 10%-11%. """)
    st.markdown("---")
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df_origin, x='race', hue='readmitted', stat="count")
    plt.xlabel('Race')
    plt.ylabel("Count")
    plt.title(f'Readmission Status By Race')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)
    race_statuses = df_origin['race'].dropna().unique()
    ncols = 4
    nrows = int(np.ceil(len(race_statuses)/ncols))
    fig,axes=plt.subplots(nrows,ncols,figsize=(8*ncols, 8*nrows))
    if nrows <= 1:
        for i, status in enumerate(race_statuses):
            subset = df_origin[df_origin['race'] == status]
            race_counts = subset['readmitted'].value_counts()
            axes[i].pie(race_counts, labels=race_counts.index, autopct='%1.1f%%', startangle=140)
            axes[i].set_title(f'Proportion of readmitted for Race = {status}')
    else:
        for i, status in enumerate(race_statuses):
            subset = df_origin[df_origin['race'] == status]
            race_counts = subset['readmitted'].value_counts()
            r = i // ncols
            c = i % ncols
            axes[r, c].pie(race_counts, labels=race_counts.index, autopct='%1.1f%%', startangle=140)
            axes[r, c].set_title(f'Proportion of readmitted for Race = {status}')
    plt.tight_layout()
    st.pyplot(plt)

with tab4:
    st.markdown(f"**Definition:** {df_variables[df_variables['name']=='weight']['description']}")
    st.markdown(""" **Findings and Observations**:  
- The most common weight groups are [75-100] (1,300 records), [50-75] (900), and [100-125] (~600). However, the early readmission rates decline as weight increases; [0-25] shows the most significant 16.7% and followed by [50-75] 11.7%, while [15-175] brackets only shows 8.6% """)
    st.markdown("---")
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df_origin, x='weight', hue='readmitted', stat="count")
    plt.xlabel('Weight')
    plt.ylabel("Count")
    plt.title(f'Readmission Status By Weight')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)
    weight_statuses = df_origin['weight'].dropna().unique()
    ncols = 4
    nrows = int(np.ceil(len(weight_statuses)/ncols))
    fig,axes=plt.subplots(nrows,ncols,figsize=(8*ncols, 8*nrows))
    if nrows <= 1:
        for i, status in enumerate(weight_statuses):
            subset = df_origin[df_origin['weight'] == status]
            weight_counts = subset['readmitted'].value_counts()
            axes[i].pie(weight_counts, labels=weight_counts.index, autopct='%1.1f%%', startangle=140)
            axes[i].set_title(f'Proportion of readmitted for Weight = {status}')
    else:
        for i, status in enumerate(weight_statuses):
            subset = df_origin[df_origin['weight'] == status]
            weight_counts = subset['readmitted'].value_counts()
            r = i // ncols
            c = i % ncols
            axes[r, c].pie(weight_counts, labels=weight_counts.index, autopct='%1.1f%%', startangle=140)
            axes[r, c].set_title(f'Proportion of readmitted for Weight = {status}')
    plt.tight_layout()
    st.pyplot(plt)