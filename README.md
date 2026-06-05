# IBM Telco Churn — ML Project

Predicting customer churn for a telecommunications company using machine learning. The goal is to identify customers at high risk of leaving the service to support targeted retention strategies.

---

## Business Problem

Customer churn is one of the most critical challenges in the telecommunications industry. Acquiring a new customer costs significantly more than retaining an existing one. This project builds a classification model capable of identifying customers likely to churn before they leave, enabling the business to take proactive action.

**Key questions:**
- What is the overall churn rate?
- Which customer characteristics are associated with higher churn risk?
- Can we predict churn with sufficient accuracy to support retention campaigns?

---

## Dataset

- **Source:** IBM Telco Customer Churn Dataset (Kaggle)
- **Size:** 7,043 customers, 21 features
- **Target variable:** `Churn` (Yes / No)
- **Churn rate:** 26.5%

---

## Project Structure

```
customer-churn-prediction/
│
├── data/
│   ├── raw/                    # Original dataset
│   └── processed/              # Train/test splits
│
├── notebooks/
│   ├── 01_eda.ipynb            # Exploratory Data Analysis
│   ├── 02_preprocessing.ipynb  # Data cleaning and feature engineering
│   └── 03_modeling.ipynb       # Model training and evaluation
│
├── images/                     # Visualizations
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Methodology

### 1. Exploratory Data Analysis
- Audit of data quality: missing values, duplicates, data types
- Detection and treatment of hidden missing values in `TotalCharges` (MAR — Missing At Random), confirmed via Mann-Whitney U test
- Univariate and bivariate analysis of numerical and categorical variables
- Correlation analysis revealing multicollinearity between `TotalCharges`, `tenure`, and `MonthlyCharges`

### 2. Preprocessing
- Imputation of 11 missing values in `TotalCharges` using `MonthlyCharges` (MAR justification)
- Removal of `customerID` (non-predictive identifier) and `TotalCharges` (multicollinearity: r=0.83 with tenure)
- One-hot encoding of categorical variables with `drop_first=True` to avoid the dummy variable trap
- Train/test split: 80/20 with stratification on the target variable
- Feature scaling with `StandardScaler` for Logistic Regression

### 3. Modeling
Four models were trained and evaluated:

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression (default) | 0.7977 | 0.6378 | 0.5508 | 0.5911 | 0.8388 |
| **Logistic Regression (balanced)** | **0.7410** | **0.5079** | **0.7781** | **0.6146** | **0.8382** |
| Random Forest (default) | 0.7885 | 0.6310 | 0.4893 | 0.5512 | 0.8209 |
| Random Forest (balanced) | 0.7878 | 0.6307 | 0.4840 | 0.5477 | 0.8205 |

**Selected model:** Logistic Regression with `class_weight='balanced'`

Cross-validation (5-fold) confirmed stable generalization: mean ROC-AUC = 0.844 (±0.014).

---

## Results

### Model Performance
The selected model achieves a **ROC-AUC of 0.8382** and detects **77.8% of churners** (recall), identifying nearly 4 out of 5 customers at risk of leaving.

### Key Findings

**Factors that increase churn risk:**
- Fiber optic internet service (strongest predictor, coefficient: +0.81)
- Electronic check payment method
- Paperless billing
- Streaming TV and Movies subscriptions

**Factors that reduce churn risk:**
- Long-term contracts (one year and two year)
- Higher tenure — longer-standing customers are significantly more loyal
- Online Security subscription
- Having dependents

### Business Recommendations
- **Convert month-to-month customers to annual contracts** — contract type is the most actionable retention lever identified by the model
- **Investigate fiber optic service** — the high churn rate may reflect a gap between pricing and perceived value
- **Promote add-on services** (Online Security, Tech Support) as retention tools
- **Target electronic check and paperless billing customers** with proactive outreach campaigns

---

## Technologies

- Python 3.14
- pandas, numpy
- matplotlib, seaborn
- scikit-learn
- scipy
- Jupyter Notebook

---

## How to Run

```bash
# Clone the repository
git clone https://github.com/AlexanderSc21/customer-churn-prediction.git

# Install dependencies
pip install -r requirements.txt

# Run notebooks in order
# 01_eda.ipynb → 02_preprocessing.ipynb → 03_modeling.ipynb
```

---

## Author

Alexander Sinte
[GitHub](https://github.com/AlexanderSc21) · [LinkedIn](https://www.linkedin.com/in/tu-perfil)