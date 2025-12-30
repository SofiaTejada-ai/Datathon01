# Loan Disbursement Prediction (Supervised ML)

Machine learning project that predicts **average disbursed loan amounts** (`avg_disbursed_loan`) using engineered financial features and tree-based models (XGBoost, Random Forest). Built as a team project and recognized with a **Best Supervised Model** award in a datathon setting.

## Overview
This repository contains a notebook-based pipeline for:
- Data loading + exploratory analysis
- Feature engineering (financial ratios and projections)
- Model training + evaluation (regression)
- Hyperparameter tuning (`RandomizedSearchCV`) and 3-fold cross-validation (`KFold`)
- Generating a `submission.csv` file for Kaggle-style submission workflows

## Highlights
- Models: **XGBoost**, **Random Forest**
- Feature engineering examples:
  - Tuition-to-income ratio
  - Career pay projection features
  - Additional financial indicators derived from the dataset
- Validation: **K-Fold cross-validation (3 splits)**
- Optimization: **RandomizedSearchCV** for hyperparameter tuning
- Metrics: **RMSE** and **R²** (reported in-notebook)
- Recognition: **Best Supervised Model** award (team project)

## Tech Stack
- Python
- XGBoost
- scikit-learn
- pandas, NumPy
- Matplotlib, Seaborn
- Jupyter

## Repository Contents
- `datathon-2025-v2 (1).ipynb` (main notebook)
- `requirements.txt`
- `scripts/download_data.py` (downloads Kaggle competition files into `data/`)
- `LICENSE`

---

## Quickstart (Local)

### 1) Clone + install
```
git clone https://github.com/SofiaTejada-ai/Datathon01.git
cd Datathon01

python -m venv env
source env/bin/activate    # macOS/Linux
# env\Scripts\activate     # Windows

pip install -r requirements.txt
```

2) Download the dataset (Kaggle competition)

This repo does not include the dataset (competition rules). Download it into data/ using the script below.

First, get your Kaggle API token:

Kaggle -> Profile -> Account -> Create New API Token (downloads kaggle.json)

Then run:

```
mkdir -p ~/.kaggle
mv ~/Downloads/kaggle.json ~/.kaggle/kaggle.json
chmod 600 ~/.kaggle/kaggle.json

python scripts/download_data.py
```

After running the script, you should have:
```
data/
  train.csv
  test.csv
  sample_submission.csv
```
3) Run the notebook
```
jupyter notebook

```
Open and run:

datathon-2025-v2 (1).ipynb

Notes

The notebook is configured to load data from:

data/train.csv

data/test.csv

data/sample_submission.csv

If you see import errors (ModuleNotFoundError), make sure you installed dependencies in the same environment that your notebook kernel is using.

For compatibility across different scikit-learn versions, RMSE is computed as np.sqrt(mean_squared_error(...)) in the notebook.

Results

Performance is reported in-notebook using a validation split and regression metrics (RMSE, R²).

Award: Best Supervised Model (team project, datathon).
