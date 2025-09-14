import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Time In Hospital vs Number of Diagnoses (LACE)")

df_variables = st.session_state["df_variables"]
df_origin = st.session_state["df_origin"]

st.markdown(""" **Findings and Observations**:  
- In general, we observe that the more diagnoses a patient has (11-16), the longer the median length of their hospital stay. However, patients with low to moderate number of diagnoses (2-9), and thereby shorter lengths of hospital stay, had higher instances of early readmission. This likely indicates a clinical gap in which patients with a lower number of diagnoses should not be subjected to shorter hospital stays.""")
st.markdown("---")

LACE_df = df_origin.iloc[:,[9,6,4,21,16,49]]

sns.boxplot(data=LACE_df, y='time_in_hospital', x='number_diagnoses', hue='readmitted', palette='Set2')
plt.title("Time In Hospital vs Number of Diagnoses (LACE)")
st.pyplot(plt)