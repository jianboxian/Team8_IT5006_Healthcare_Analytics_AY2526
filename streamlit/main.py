import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Get project root (two levels up from this file)
ROOT = Path(__file__).resolve().parent.parent  

#st.title("Data Analysis and Visualization ")
st.set_page_config(layout="wide")
df_variables = pd.read_csv(ROOT / "streamlit" / "data" / "diabetes_variables.csv")
df_origin = pd.read_csv(ROOT / "streamlit" / "data" / "diabetes_data.csv")

st.session_state["df_variables"] = df_variables
st.session_state["df_origin"] = df_origin
show_pages = {
    "Variable Explorations":[
        st.Page(ROOT / "streamlit" / "pages" / "Variable_Exploration" / "variable_exploration.py",title="Variable Overview",icon="🗒️"),
        st.Page(ROOT / "streamlit" / "pages" / "Variable_Exploration" / "categorical_variable_frequency_table.py",title="Categorical Variable Frequency Table",icon="📋"),
        st.Page(ROOT / "streamlit" / "pages" / "Variable_Exploration" / "descriptive_stats_table.py",title="Descriptive Statistics Table",icon="📈"),
        st.Page(ROOT / "streamlit" / "pages" / "Variable_Exploration" / "missing_values_by_variable.py",title="Missing Values by Variable",icon="❓"),
        st.Page(ROOT / "streamlit" / "pages" / "Variable_Exploration" / "unique_values_by_variable.py",title="Unique Values by Variable",icon="🔢"),
        st.Page(ROOT / "streamlit" / "pages" / "Variable_Exploration" / "readmitted_histogram.py",title="Dependent Variable Histogram",icon="📊"),
    ],
    "Univariate Analysis by Category":[
        st.Page(ROOT / "streamlit" / "pages" / "Univariate_Analysis" / "UA_Demographics.py",title="Demographics Histogram",icon="📊"),
        st.Page(ROOT / "streamlit" / "pages" / "Univariate_Analysis" / "UA_Admission_Details.py",title="Admission Details Histogram",icon="📊"),
        st.Page(ROOT / "streamlit" / "pages" / "Univariate_Analysis" / "UA_Diagnoses.py",title="Diagnoses Histogram",icon="📊"),
        st.Page(ROOT / "streamlit" / "pages" / "Univariate_Analysis" / "UA_Healthcare_Provider.py",title="Healthcare Provider Histogram",icon="📊"),
        st.Page(ROOT / "streamlit" / "pages" / "Univariate_Analysis" / "UA_Clinical_Metrics_Histogram.py",title="Clinical Metrics Histogram",icon="📊"),
        st.Page(ROOT / "streamlit" / "pages" / "Univariate_Analysis" / "UA_Laboratory_Results.py",title="Laboratory Results Histogram",icon="📊"),
        st.Page(ROOT / "streamlit" / "pages" / "Univariate_Analysis" / "UA_Medications.py",title="Medications Histogram",icon="📊"),
        st.Page(ROOT / "streamlit" / "pages" / "Univariate_Analysis" / "UA_Treatment_Changes.py",title="Treatment Changes Histogram",icon="📊"),
    ],
    "Bivariate Analysis":[
        # st.Page("./pages/pair_plot_for_showing_the_distribution.py",title="Pair Plot for Showing the Distribution",icon="📉"),
        # st.Page("./pages/Boxplot_for_showing_the_distribution.py",title="Box Plot for Showing the Distribution",icon="🧊"),
        st.Page(ROOT / "streamlit" / "pages" / "Bivariate_Analysis" / "BA_Demographics.py",title="Demographics",icon="🥧"),
        st.Page(ROOT / "streamlit" / "pages" / "Bivariate_Analysis" / "BA_Admission_Details.py",title="Admission Details",icon="🥧"),
        st.Page(ROOT / "streamlit" / "pages" / "Bivariate_Analysis" / "BA_Diagnoses.py",title="Diagnoses",icon="🥧"),
        st.Page(ROOT / "streamlit" / "pages" / "Bivariate_Analysis" / "BA_Healthcare_Provider.py",title="Healthcare Provider",icon="🥧"),
        st.Page(ROOT / "streamlit" / "pages" / "Bivariate_Analysis" / "BA_Clinical_Metrics_BoxPlot.py",title="Clinical Metrics BoxPlot",icon="🧊"),
        ##redo this one ####st.Page("./pages/Bivariate_Analysis/BA_Clinical_Metrics.py",title="Clinical Metrics",icon="📉"),
        st.Page(ROOT / "streamlit" / "pages" / "Bivariate_Analysis" / "BA_Laboratory_Results.py",title="Laboratory Results",icon="🥧"),
        st.Page(ROOT / "streamlit" / "pages" / "Bivariate_Analysis" / "BA_Medications.py",title="Medications",icon="🥧"),
        st.Page(ROOT / "streamlit" / "pages" / "Bivariate_Analysis" / "BA_Treatment_Changes.py",title="Treatment Changes",icon="🥧"),
    ],
    "Multivariate Analysis":[
        st.Page(ROOT / "streamlit" / "pages" / "Multivariate_Analysis" /"MA_Correlation_Heatmap.py",title="Correlation Heatmap",icon="🔢"),
        st.Page(ROOT / "streamlit" / "pages" / "Multivariate_Analysis" /"MA_Time_in_Hospital_vs_No_of_Diagnoses.py",title="Time In Hospital vs Number of Diagnoses (LACE)",icon="📐"),
        st.Page(ROOT / "streamlit" / "pages" / "Multivariate_Analysis" /"MA_Age_vs_No_of_Diagnoses.py",title="Age vs Number of Diagnoses (PCi)",icon="📐"),
        st.Page(ROOT / "streamlit" / "pages" / "Multivariate_Analysis" /"MA_Number_of_Procedures_vs_No_of_Lab_Procedures.py",title="Number of Procedures vs Number of Lab Procedures",icon="📐"),
    ],
    "Other Key Insights":[
        st.Page(ROOT / "streamlit" / "pages" / "Key_Insights" /"readmission_vs_medical_specialty.py",title="Medical Specialty VS Readmission",icon="🧠"),
        st.Page(ROOT / "streamlit" / "pages" / "Key_Insights" /"readmission_vs_insulin.py",title="Insulin VS Readmission",icon="🧠"),
    ],

}

pg =st.navigation(show_pages)
pg.run()