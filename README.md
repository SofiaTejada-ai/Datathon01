Loan Disbursement Prediction Model
Project Overview

This project focuses on developing a highly accurate supervised learning model to predict the average disbursed loan using advanced machine learning techniques. The model achieved 96% accuracy and was recognized with the Best Supervised Model award for its predictive performance and innovation.

Key Features:
* Supervised Learning Model: Utilized XGBoost and RandomForest for high-accuracy loan predictions.
* Feature Engineering: Developed advanced features, including:
Tuition-to-income ratios
Career pay projections
Other relevant financial indicators
* Model Optimization:
 - Cross-validation: Implemented KFold (3 splits) to improve generalization.
 - Hyperparameter tuning: Applied RandomizedSearchCV to optimize model efficiency.
* Data Preprocessing Pipelines:
 - Missing value imputation
- Feature scaling and transformation
- Ensured clean and structured input data for robust predictions
* Collaboration & Award Recognition:
 - Worked closely with a team to refine the model.
 - Achieved the Best Supervised Model award for outstanding predictive accuracy and methodological innovation.

Tech Stack
*Programming Language: Python
*Libraries & Tools:
 - XGBoost
 - Scikit-learn
- Pandas
- NumPy
- Matplotlib & Seaborn (for data visualization)

Installation process:

Kaggle Link
Access the project on Kaggle: https://www.kaggle.com/code/sofiatejada01/datathon-2025-v2/edit

1. Clone the repository:
git clone https://github.com/SofiaTejada-ai/Datathon-2025-v2.git
cd Datathon-2025-v2

2. Create a virtual environment (recommended):
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

4. Install dependencies:
pip install -r requirements.txt

5.Run the model training script:
python train_model.py

*Usage:
Modify the input dataset in the data/ folder.
Adjust hyperparameters in the config.json file (if applicable).
Run predict.py to generate loan predictions for new data.


Contributors
Sofia Tejada – Model development, data analyzer
Christopher Chan, Matthew Marrietta, Helen Ton – Data preprocessing, analysis, validation

Contact:
For any inquiries, please reach out via:
Email: sofiatejada001@gmail.com
LinkedIn: https://www.linkedin.com/public-profile/settings?trk=d_flagship3_profile_self_view_public_profile
