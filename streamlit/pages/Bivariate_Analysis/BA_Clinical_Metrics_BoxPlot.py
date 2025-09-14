import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Clinical Metrics Distribution BoxPlots")

df_variables = st.session_state["df_variables"]
df_origin = st.session_state["df_origin"]

list_of_cols = ['num_lab_procedures', 'num_procedures', 'num_medications','number_outpatient','number_emergency','number_inpatient','number_diagnoses']

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(list_of_cols)


for index, col in enumerate(list_of_cols):
    with eval(f"tab{index+1}"):
        st.markdown(f"**Definition:** {df_variables[df_variables['name']==col]['description']}")
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='readmitted', y= col, data=df_origin)
        plt.title(f'{col} Distribution by Readmission Status')
        plt.xlabel(col)
        plt.ylabel('Readmission Status')
        plt.tight_layout()
        st.pyplot(plt)

# for col in ['number_inpatient','number_emergency','number_diagnoses',
#             'number_outpatient','num_medications','time_in_hospital']:
#     print(f'\n=== {col} average by Readmission ===')
#     print(df_origin.groupby('readmitted')[col].mean())
    
# for col in ['number_inpatient','number_emergency','number_diagnoses',
#             'number_outpatient','num_medications','time_in_hospital']:
#     plt.figure(figsize=(8,4))
#     sns.boxplot(x='readmitted', y=col, data=df_origin)
#     plt.title(f'{col} vs Readmission')
#     plt.show()

# ct = pd.crosstab(df_origin['readmitted'], df_origin['medical_specialty'])

# print('\n=== crosstab: readmited vs medical_specialty ===')
# display(ct)

# from scipy.stats import chi2_contingency
# chi2, p, dof, expected = chi2_contingency(ct)
# print(f'chi2 = {chi2}, p = {p}, dof = {dof}')
# if p < 0.05:
#     print ('Reject null hypothesis: There is a significant association between readmission and medical specialty.')
# else:
#     print ('Fail to reject null hypothesis: There is no significant association between readmission and medical specialty.')
