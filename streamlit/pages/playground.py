import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns




tab1, tab2 = st.tabs(["Summary", "Histograms"])

with tab1:
    st.write("Content for Summary tab")

with tab2:
    st.write("Content for Histograms tab")

# st.title("Box Plot for Showing the Distribution")

# df_variables = st.session_state["df_variables"]
# df_origin = st.session_state["df_origin"]
# df_variables_integer = df_variables[df_variables["type"] == "Integer"]["name"]

# plt.figure(figsize=(15, 10))
# sns.heatmap(df_origin[df_variables_integer].corr(), annot=True, fmt='.2f', cmap='Blues', linewidths=2)
# plt.title('Correlation Heatmap')
# st.pyplot(plt)