import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns


st.title("Categorical Variable Frequency Table")

df_variables = st.session_state["df_variables"]
df_origin = st.session_state["df_origin"]

rows = []
for col in df_origin[[i for i in df_variables[df_variables["type"]=="Categorical"]["name"]]].columns:
    dftmp = df_origin[col].value_counts()
    for subcat,qty in zip(dftmp.index,dftmp.values):
        rows.append({"Column Name": col, "Catergory": subcat, "Count": qty})
    df_variable_freq=pd.DataFrame(rows)
st.dataframe(df_variable_freq, use_container_width=True, height=600)