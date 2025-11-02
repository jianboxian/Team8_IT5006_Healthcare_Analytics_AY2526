# Team 8 — IT5006 Healthcare Analytics: Diabetes Readmission Project

A consolidated overview of the data exploration, model development, and deployed Streamlit application for the “Diabetes 130-US hospitals for years 1999–2008” dataset.

## Project overview

- Objective: Explore factors associated with patient readmission and build predictive models for readmission risk.
- Dataset: Diabetes 130-US hospitals (1999–2008), sourced from UCI ML Repository (features include demographics, admission details, diagnoses, procedures, medications, labs, and outcomes).
- Deliverables:
  - Milestone 1: Exploratory Data Analysis (EDA) notebooks (by team members)
  - Milestone 2: Model training and evaluation notebooks (by team members + combined notebook)
  - Streamlit app: Interactive data exploration and insights

## Repository structure

```
Project_Diabetes/
├─ requirements.txt
├─ Milestone 1 Jupyter Notebook/                  # EDA notebooks (per member)
├─ Milestone 2 Jupyter Notebook/                  # Model training notebooks (per member + combined)
│  ├─ [YA_final] IT5006_Data_preprocessing_and_model_deployment.ipynb
│  ├─ Team8 Milestone 2 Jupyter Notebook.ipynb
│  └─ Model performance summary tables.zip        # High-resolution summary images
└─ streamlit/
   ├─ main.py                                     # Streamlit entrypoint
   ├─ data/
   │  ├─ diabetes_data.csv                        # Full dataset extract
   │  └─ diabetes_variables.csv                   # Feature descriptions/metadata
   └─ pages/                                      # App pages (rendered as sidebar sections)
      ├─ Univariate_Analysis/
      ├─ Bivariate_Analysis/
      └─ other analysis utilities
```

## Milestones and notebooks

### Milestone 1 — Exploratory Data Analysis (EDA)
- Folder: `Milestone 1 Jupyter Notebook/`
- Content: Individual EDA notebooks authored by team members, covering:
  - Data understanding and schema checks
  - Missing values and imputation considerations and display
  - Summarised view of all features
  - Univariate and bivariate summaries (distributions, frequencies, correlations)
  - Early observations to inform feature engineering and modeling

### Milestone 2 — Model development and evaluation
- Folder: `Milestone 2 Jupyter Notebook/`

Key artifacts:
- `[YA_final] IT5006_Data_preprocessing_and_model_deployment.ipynb` (Yu)
  - Highlights: Comprehensive feature engineering (e.g., encoding strategies, aggregations, derived features) and experiments with SMOTE to address class imbalance.
- `Team8 Milestone 2 Jupyter Notebook.ipynb`
  - Combined team work integrating preprocessing, modeling pipelines, evaluation metrics, and comparative results.
- `Model performance summary tables.zip`
  - High-resolution images exported from the combined notebook summarizing model performance (e.g., accuracy, AUC/ROC, precision/recall, confusion matrices), suitable for reports.

## Streamlit application

- Live app URL: https://team8it5006healthcareanalyticsay2526-nmkexjgpy5gkwvgorkawkr.streamlit.app/
- Source: `streamlit/`
  - `main.py` is the app entrypoint (home page and navigation)
  - `streamlit/data/` contains the working dataset extracts and variable dictionary
  - `streamlit/pages/` houses feature-specific pages organized by analysis categories (e.g., Univariate, Bivariate), which appear as sidebar tabs in the app

### Run the streamlit app locally

Prerequisites:
- Python 3.10+ recommended
- Install project dependencies

```powershell
# From the project root
pip install -r .\requirements.txt

# Launch Streamlit (from project root)
python -m streamlit run .\streamlit\main.py

```

Common options:
```powershell
# Change port
python -m streamlit run .\streamlit\main.py --server.port 8502

# Listen on all interfaces (for LAN testing)
python -m streamlit run .\streamlit\main.py --server.address 0.0.0.0
```

## Data

- Location: `streamlit/data/`
  - `diabetes_data.csv`: Processed/extracted dataset used within the app
  - `diabetes_variables.csv`: Variable names, types, and human-readable descriptions
- Original source: UCI Machine Learning Repository — “Diabetes 130-US hospitals for years 1999–2008”.

## How this repository is used in reports

- The team’s report materials are primarily extracted from `Milestone 2 Jupyter Notebook/Team8 Milestone 2 Jupyter Notebook.ipynb`.
- High-resolution performance tables and figures are packaged in `Model performance summary tables.zip` for publication quality.

## Notes and tips

- Streamlit pages use session state to share loaded data across pages (e.g., `df_origin`, `df_variables`). Keep the data CSVs in `streamlit/data/` so paths remain portable inside the app.
- For categorical frequency plots and outlier checks, prefer:
  - Boxplots (with optional swarm overlays) for outlier visualization
  - Count plots or pie charts for categorical distributions (depending on audience)
- For new pages, place them in `streamlit/pages/` to appear automatically in the app’s sidebar.

## Maintenance

- Pin or review `requirements.txt` regularly to ensure reproducibility.
- If data schema changes, update `diabetes_variables.csv` and any dependent preprocessing logic.
- Keep the live app URL updated in this README if deployment endpoints change.

---

For questions or contributions, please open an issue or PR in this repository.
