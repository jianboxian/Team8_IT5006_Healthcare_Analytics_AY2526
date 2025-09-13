import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Demographic Distribution Histograms")

df_variables = st.session_state["df_variables"]
df_origin = st.session_state["df_origin"]
readmitted_statuses = df_origin['readmitted'].unique()


tab1, tab2, tab3, tab4 = st.tabs(['Age', 'Gender', 'Race','Weight'])


with tab1:
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