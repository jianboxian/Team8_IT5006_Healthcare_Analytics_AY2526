import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Age vs Number of Diagnoses (PCi)")

df_variables = st.session_state["df_variables"]
df_origin = st.session_state["df_origin"]

st.markdown(""" **Findings and Observations**:  
- We observe that patients from the middle to older age groups [40-50] and [50-60] tend to have a higher median of diagnoses as compared to those in younger age groups. However, the proportion of patient readmissions (both early and late) is higher in younger age groups [0-10] to [30-40]. This indicates age as a higher influence of hospital readmission as compared to number of diagnoses. Another possible explanation is that patients from the older age groups might have passed away and thus not be readmitted, thereby skewing the readmission frequency in those datasets.""")
st.markdown("---")

PCi_df = df_origin.iloc[:,[14,4,21,48,49]]

sns.boxplot(data=PCi_df, x='age', y='number_diagnoses', hue='readmitted', palette='Set2')
plt.title("Age vs Number of Diagnoses (PCi)")
st.pyplot(plt)