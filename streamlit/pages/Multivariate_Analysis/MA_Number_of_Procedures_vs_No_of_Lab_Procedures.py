import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Number of Procedures vs Number of Lab Procedures")

df_variables = st.session_state["df_variables"]
df_origin = st.session_state["df_origin"]

st.markdown(""" **Findings and Observations**:  
-  We observe that the median number of lab procedures increases with increasing number of procedures undergone by patients, indicating a general proportional relationship between these 2 attributes. Furthermore, the frequency of readmission does not increase with an increasing number of procedures. This suggests that we can remove the number of lab procedures from consideration (dimension reduction) without losing key information.""")
st.markdown("---")



sns.boxplot(data=df_origin, y='num_lab_procedures', x='num_procedures', hue='readmitted', palette='Set2')
plt.title("Number of Procedures vs Number of Lab Procedures")
st.pyplot(plt)