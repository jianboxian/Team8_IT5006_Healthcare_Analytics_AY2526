import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns

st.title("LACE Multivariate Plot: Time In Hospital vs Number of Diagnoses")

df_variables = st.session_state["df_variables"]
df_origin = st.session_state["df_origin"]


LACE_df = df_origin.iloc[:,[9,6,4,21,16,49]]

sns.boxplot(data=LACE_df, y='time_in_hospital', x='number_diagnoses', hue='readmitted', palette='Set2')
plt.title("LACE Multivariate Plot: Time In Hospital vs Number of Diagnoses")
st.pyplot(plt)