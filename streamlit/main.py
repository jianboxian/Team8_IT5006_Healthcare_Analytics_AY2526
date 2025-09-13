import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns


#st.title("Data Analysis and Visualization ")
st.set_page_config(layout="wide")
df_variables = pd.read_csv("./data/diabetes_variables.csv")
df_origin = pd.read_csv("./data/diabetes_data.csv")

st.session_state["df_variables"] = df_variables
st.session_state["df_origin"] = df_origin
show_pages = {
    "Variable Explorations":[
        st.Page("./pages/variable_exploration.py",title="Variable Explorations",icon="📊"),
        st.Page("./pages/categorical_variable_frequency_table.py",title="Categorical Variable Frequency Table",icon="📋"),
        st.Page("./pages/descriptive_stats_table.py",title="Descriptive Statistics Table",icon="📈"),
        st.Page("./pages/missing_values_by_variable.py",title="Missing Values by Variable",icon="❓"),
        st.Page("./pages/unique_values_by_variable.py",title="Unique Values by Variable",icon="🔢"),
    ],
    "Univariate Analysis by Category":[
        st.Page("./pages/Univariate_Analysis/UA_Demographics.py",title="Demographics",icon="📉"),
        st.Page("./pages/Univariate_Analysis/UA_Admission_Details.py",title="Admission Details",icon="📉"),
        st.Page("./pages/Univariate_Analysis/UA_Diagnoses.py",title="Diagnoses",icon="📉"),
        st.Page("./pages/Univariate_Analysis/UA_Healthcare_Provider.py",title="Healthcare Provider",icon="📉"),
        st.Page("./pages/Univariate_Analysis/UA_Clinical_Metrics.py",title="Clinical Metrics",icon="📉"),
        st.Page("./pages/Univariate_Analysis/UA_Laboratory_Results.py",title="Laboratory Results",icon="📉"),
        st.Page("./pages/Univariate_Analysis/UA_Medications.py",title="Medications",icon="📉"),
        st.Page("./pages/Univariate_Analysis/UA_Treatment_Changes.py",title="Treatment Changes",icon="📉"),
    ],
    "Bivariate Analysis":[
        # st.Page("./pages/pair_plot_for_showing_the_distribution.py",title="Pair Plot for Showing the Distribution",icon="📉"),
        # st.Page("./pages/Boxplot_for_showing_the_distribution.py",title="Box Plot for Showing the Distribution",icon="🧊"),
        st.Page("./pages/Bivariate_Analysis/BA_Demographics.py",title="Demographics",icon="📉"),
        st.Page("./pages/Bivariate_Analysis/BA_Admission_Details.py",title="Admission Details",icon="📉"),
        st.Page("./pages/Bivariate_Analysis/BA_Diagnoses.py",title="Diagnoses",icon="📉"),
        st.Page("./pages/Bivariate_Analysis/BA_Healthcare_Provider.py",title="Healthcare Provider",icon="📉"),
        ##redo this one ####st.Page("./pages/Bivariate_Analysis/BA_Clinical_Metrics.py",title="Clinical Metrics",icon="📉"),
        st.Page("./pages/Bivariate_Analysis/BA_Laboratory_Results.py",title="Laboratory Results",icon="📉"),
        st.Page("./pages/Bivariate_Analysis/BA_Medications.py",title="Medications",icon="📉"),
        st.Page("./pages/Bivariate_Analysis/BA_Treatment_Changes.py",title="Treatment Changes",icon="📉"),
    ],
    "Multivariate Analysis":[
        st.Page("./pages/Correlation_Heatmap.py",title="Correlation Heatmap",icon="📊"),
    ],
    "Play Ground":[
        st.Page("./pages/playground.py",title="Playground",icon="🎮"),
    ],


}

pg =st.navigation(show_pages)
pg.run()