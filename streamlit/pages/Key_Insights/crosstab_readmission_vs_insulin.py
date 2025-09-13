import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency

st.title("Crosstab: Readmission VS Insulin")

df_variables = st.session_state["df_variables"]
df_origin = st.session_state["df_origin"]


READMITTED_COL = 'readmitted'
drug_cols = df_origin.columns[24:49]

for drug in drug_cols:
    st.write(f"\n==={drug}===")
    counts = df_origin[drug].value_counts().sort_index()
    st.write("counts")
    st.dataframe(counts)

    readmitted_mask = df_origin[READMITTED_COL] != 'NO'
    count_readmit = df_origin.loc[readmitted_mask, drug].value_counts().sort_index()
    st.write("counts (readmitted)")
    st.dataframe(count_readmit)

    fig, ax = plt.subplots(1,2, figsize=(12,4),sharey=True)

    counts.plot(kind = 'bar', ax=ax[0], title=f'All patients - {drug}')
    count_readmit.plot(kind = 'bar', ax=ax[1], title=f'Readmitted patients - {drug}')

    plt.suptitle(f'Drug: {drug}')
    plt.tight_layout()
    st.pyplot(plt)


for drug in ['insulin', 'diabetesMed']:
    st.write(f"\n==={drug}=== vs Readmission===")

    ct = pd.crosstab(df_origin[drug], df_origin['readmitted'])
    st.dataframe(ct)
    chi2, p, dof, expected = chi2_contingency(ct)
    st.write(f'chi2 = {chi2}, p = {p}, dof = {dof}')
    if p < 0.05:
        st.write ('Reject null hypothesis: There is a significant association between readmission and the drug.')
    else:
        st.write ('Fail to reject null hypothesis: There is no significant association between readmission and the drug.')

    ct_ratio = ct.div(ct.sum(axis=1), axis=0)
    st.write(f'\n=== crosstab (ratio): readmitted vs {drug} ===')
    st.dataframe(ct_ratio)

    ct_ratio.plot(kind='bar', stacked=True, figsize=(8,5), cmap='Pastel1')
    plt.title(f'Readmission distribution by {drug}')
    plt.xlabel(drug)
    plt.ylabel('Proportion')
    plt.xticks(rotation=0)
    plt.legend(title='Readmission', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    st.pyplot(plt)