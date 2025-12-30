# Loan Disbursement Prediction Model

Supervised a regression learning project that predicts average loan disbursement amounts using engineered financial features and tree-based models. The final approach achieved strong performance and received a Best Supervised Model award.

## Overview
This project builds and evaluates machine learning models to estimate average disbursed loan amounts. It includes feature engineering, preprocessing pipelines, cross-validation, and hyperparameter tuning to improve generalization and reliability.

## Highlights
- Models: XGBoost, Random Forest
- Feature engineering examples:
  - Tuition-to-income ratio
  - Career pay projection features
  - Additional financial indicators derived from the dataset
- Validation: K-Fold cross-validation (3 splits)
- Optimization: RandomizedSearchCV for hyperparameter tuning
- Preprocessing:
  - Missing value imputation
  - Feature scaling and transformations (as needed by the pipeline)
- Recognition: Best Supervised Model award (team project)

## Tech Stack
- Python
- XGBoost
- scikit-learn
- pandas, NumPy
- Matplotlib (and Seaborn, if used in notebooks)

## Repository Structure
- `datathon-2025-v2 (1).ipynb` 
## Setup
```
git clone https://github.com/SofiaTejada-ai/Datathon01.git
cd Datathon-2025-v2

python -m venv env
source env/bin/activate    # macOS/Linux
# env\Scripts\activate     # Windows



Usage Notes

Place or replace the dataset in data/

Adjust model settings in config.json (if present)

Run training to reproduce metrics, then run prediction for new inputs

Results

Reported performance: 96% accuracy (see notebook / training output for details)

Award: Best Supervised Model (datathon)

