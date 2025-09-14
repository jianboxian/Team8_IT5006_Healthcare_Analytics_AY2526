import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Variable Explorations")

df_variables = st.session_state["df_variables"]
df_origin = st.session_state["df_origin"]

# pd.set_option('display.max_colwidth', None)
# from IPython.display import display
# df_variables['Unique Values']=[df_origin[col].nunique() for col in df_origin.columns]
# df_variables['Missing Values Qty']=[df_origin[col].isnull().sum() for col in df_origin.columns]
# display(df_variables[['name',"type","role","Unique Values","Missing Values Qty","description"]].style.set_properties(**{'text-align': 'left'}))


pd.set_option('display.max_colwidth', None)
df_variables['Unique Values'] = [df_origin[col].nunique() for col in df_origin.columns]
df_variables['Missing Values Qty'] = [df_origin[col].isnull().sum() for col in df_origin.columns]

st.dataframe(
    df_variables[['name', 'type', 'role', 'Unique Values', 'Missing Values Qty', 'description']],
    use_container_width=True,
    height=600
)