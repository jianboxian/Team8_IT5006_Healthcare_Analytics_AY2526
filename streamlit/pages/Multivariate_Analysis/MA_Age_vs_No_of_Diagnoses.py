import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns

st.title("PCi Multivariate Plot: Age vs Number of Diagnoses")

df_variables = st.session_state["df_variables"]
df_origin = st.session_state["df_origin"]


PCi_df = df_origin.iloc[:,[14,4,21,48,49]]

sns.boxplot(data=PCi_df, x='age', y='number_diagnoses', hue='readmitted', palette='Set2')
plt.title("PCi Multivariate Plot: Age vs Number of Diagnoses")
st.pyplot(plt)