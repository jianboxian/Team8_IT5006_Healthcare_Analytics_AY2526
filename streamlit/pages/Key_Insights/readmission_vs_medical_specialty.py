import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency

st.title("Readmission VS Medical Specialty")

df_variables = st.session_state["df_variables"]
df_origin = st.session_state["df_origin"]


ct = pd.crosstab(df_origin['readmitted'], df_origin['medical_specialty'])

st.markdown(""" **Findings and Observations**: 
- This variable provides insights into the speciality of the attending physician. We filtered out specialities with fewer than 100 records and focused on top specialties by early readmission proportion.
- Our first key observation is that the Internal Medicine, Emergency/Trauma, and Family/General Practice are the most represented specialties, reflecting the primary role these departments play in diabetes-related admissions.
However, when analyzing the proportion of early readmissions, Hematology/Oncology (19.3%), Oncology (18.9%), and Nephrology (15.3%) show the highest early readmission rates. In contrast, high-volume general departments such as Internal Medicine (11.2%) and Family Practice (11.9%) have lower readmission proportions.
- This disparity suggests that patients managed by Hematology, Oncology, and Nephrology are at significantly higher risk of early readmission, likely due to the underlying severity of illness, comorbidity burden, and treatment complexity.
""")

st.markdown("---")
st.write('\n Please refer to the statistics tables below: ')
# st.dataframe(ct)


chi2, p, dof, expected = chi2_contingency(ct)
#st.write(f'chi2 = {chi2}, p = {p}, dof = {dof}')
# if p < 0.05:
#     st.write ('Reject null hypothesis: There is a significant association between readmission and medical specialty.')
# else:
#     st.write ('Fail to reject null hypothesis: There is no significant association between readmission and medical specialty.')


#Cross table for readmitted vs medical_specialty
ct = pd.crosstab(df_origin['readmitted'], df_origin['medical_specialty'])
st.dataframe(ct.iloc[:,:10])

#Convert to percentage(column wise)
ct_ratio = ct.div(ct.sum(axis=0), axis=1)

#filtering the min-case
min_cases = 100
valid_specs = ct.sum(axis=0)[ct.sum(axis=0) >= min_cases]

#Display the ratio table for valid medical specialties only
readmit_lt30 = ct_ratio.loc['<30', valid_specs.index].sort_values(ascending=False)
top15_specs = readmit_lt30.head(15).index

st.write(f'\n=== crosstab (ratio): readmited vs medical_specialty (at least {min_cases} cases) ===')
top15_summary = pd.DataFrame({
    'count_total': ct[valid_specs.index].loc['NO'].add(ct[valid_specs.index].loc['>30'], fill_value=0).add(ct[valid_specs.index].loc['<30'], fill_value=0),
    'count_<30': ct[valid_specs.index].loc['<30'],
    'prop_<30': ct_ratio.loc['<30', valid_specs.index]
}).loc[top15_specs].sort_values(by='prop_<30', ascending=False)
st.dataframe(top15_summary)

#Chi-square test
from scipy.stats import chi2_contingency
chi2, p, dof, expected = chi2_contingency(ct)
print(f'chi2 = {chi2}, p = {p}, dof = {dof}')
if p < 0.05:
    print ('Reject null hypothesis: There is a significant association between readmission and medical specialty.')
else:
    print ('Fail to reject null hypothesis: There is no significant association between readmission and medical specialty.')


#top 20 medical specialties with highest readmission rate (<30 days)
plt.figure(figsize=(10,5))
readmit_lt30.head(20).plot(kind='bar')
plt.title('Top 20 Medical Specialties with Highest Readmission Rate (<30 days)')
plt.xlabel('Medical Specialty')
plt.ylabel('Proportion of Readmission (<30 days)')
plt.xticks(rotation=90)
plt.tight_layout()
st.pyplot(plt)


#Stacked bar chart for readmission by medical specialty (top 15)
ct_med_ratio = ct.div(ct.sum(axis=0), axis=1)
ct_med_ratio_T = ct_med_ratio[top15_specs].T
ct_med_ratio_T.plot(kind='bar', stacked=True, figsize=(12,6), cmap='tab20')
plt.title('Proportion of Readmission by Medical Specialty')
plt.xlabel('Medical Specialty')
plt.ylabel('Proportion')
plt.xticks(rotation=90)
plt.legend(title='Readmission', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
st.pyplot(plt)