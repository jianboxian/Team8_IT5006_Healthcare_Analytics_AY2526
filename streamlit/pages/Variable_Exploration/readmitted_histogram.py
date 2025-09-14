import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Readmission Distribution Histograms & Pie Chart")

df_variables = st.session_state["df_variables"]
df_origin = st.session_state["df_origin"]

plt.figure(figsize=(10, 6))
sns.histplot(data=df_origin['readmitted'], bins=5, color='skyblue')
plt.title('Readmission Count Distribution')
plt.xlabel('Readmission')
plt.ylabel('Count')
plt.tight_layout()
st.pyplot(plt)

plt.figure(figsize=(8, 8))
readmitted_counts = df_origin['readmitted'].value_counts()
plt.pie(readmitted_counts, labels=readmitted_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Readmission Distribution Pie Chart')
plt.axis('equal')
st.pyplot(plt)
