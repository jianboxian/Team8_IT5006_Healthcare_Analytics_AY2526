import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Number of Procedures vs Number of Lab Procedures")

df_variables = st.session_state["df_variables"]
df_origin = st.session_state["df_origin"]


sns.boxplot(data=df_origin, y='num_lab_procedures', x='num_procedures', hue='readmitted', palette='Set2')
plt.title("Number of Procedures vs Number of Lab Procedures")
st.pyplot(plt)