# House Price Prediction Using Linear Regression

## 1. Project Overview

This project focuses on predicting house prices using Machine Learning techniques, specifically Linear Regression.

The model predicts house prices based on various features such as area, number of bedrooms, bathrooms, stories, parking facilities, air conditioning, furnishing status, and other housing characteristics.

The main objective is to understand the complete Machine Learning workflow, from data collection and analysis to model training, evaluation, and prediction.

## 2. Objectives

- Understand and analyze the housing dataset.
- Perform Exploratory Data Analysis (EDA).
- Identify relationships between housing features and house prices.
- Clean and preprocess the dataset.
- Build a Linear Regression model.
- Evaluate the model using performance metrics.
- Visualize actual and predicted house prices.
- Predict the price of a new house using the trained model.

## 3. Technologies and Libraries Used

### Programming Language
- Python 3.10

### Development Environment
- Visual Studio Code

### Python Libraries
- Pandas – Data manipulation and analysis.
- NumPy – Numerical calculations.
- Matplotlib – Data visualization.
- Seaborn – Statistical visualization.
- Scikit-learn – Machine Learning model development and evaluation.
- Joblib – Saving and loading the trained model.

## 4. Dataset Description

The project uses a Housing Price Prediction dataset.

- Total Records: 545
- Total Columns: 13
- Target Variable: `price`

### Dataset Features

| Feature | Description |
|---|---|
| price | Price of the house |
| area | Area of the house |
| bedrooms | Number of bedrooms |
| bathrooms | Number of bathrooms |
| stories | Number of floors |
| mainroad | Whether the house is connected to the main road |
| guestroom | Availability of a guest room |
| basement | Availability of a basement |
| hotwaterheating | Availability of hot water heating |
| airconditioning | Availability of air conditioning |
| parking | Number of parking spaces |
| prefarea | Whether the house is in a preferred area |
| furnishingstatus | Furnishing condition of the house |

## 5. Project Structure

```text
House_Price_Prediction/
│
├── dataset/
│   └── Housing.csv
│
├── notebooks/
│
├── outputs/
│   ├── price_distribution.png
│   ├── area_vs_price.png
│   ├── bedrooms_vs_price.png
│   ├── furnishing_vs_price.png
│   ├── correlation_heatmap.png
│   ├── processed_housing.csv
│   ├── actual_vs_predicted.png
│   └── house_price_model.pkl
│
├── src/
│   ├── test.py
│   ├── data_analysis.py
│   ├── eda.py
│   ├── correlation.py
│   ├── preprocessing.py
│   ├── train_model.py
│   ├── visualize_results.py
│   └── predict_price.py
│
├── venv/
│
└── README.md
```

## 6. Project Workflow

### Step 1: Environment Setup

Installed Python and the required libraries.

### Step 2: Data Loading

Loaded the Housing.csv dataset using Pandas.

Checked:
- First five records.
- Dataset shape.
- Column names.
- Dataset information.
- Missing values.

### Step 3: Exploratory Data Analysis (EDA)

Performed exploratory data analysis using Matplotlib and Seaborn.

Created the following visualizations:

1. House Price Distribution
2. Area vs House Price
3. Bedrooms vs House Price
4. Furnishing Status vs House Price

### Step 4: Correlation Analysis

Performed correlation analysis to identify the relationship between different housing features and house prices.

Important correlation results:

| Feature | Correlation with Price |
|---|---:|
| Area | 0.5360 |
| Bathrooms | 0.5175 |
| Air Conditioning | 0.4530 |
| Stories | 0.4207 |
| Parking | 0.3844 |
| Bedrooms | 0.3665 |
| Preferred Area | 0.3298 |
| Main Road | 0.2969 |
| Guest Room | 0.2555 |
| Basement | 0.1871 |
| Hot Water Heating | 0.0931 |
| Semi-furnished | 0.0637 |
| Unfurnished | -0.2806 |

Area has the strongest positive correlation with house prices among the input features.

### Step 5: Data Preprocessing

Converted categorical values into numerical representations.

- Converted Yes/No values into 1/0.
- Applied One-Hot Encoding to furnishing status.
- Saved the processed dataset as `processed_housing.csv`.

### Step 6: Train-Test Split

Separated the dataset into training and testing sets.

- Training Data: 80%
- Testing Data: 20%
- Random State: 42

Training Records: 436

Testing Records: 109

### Step 7: Model Training

Developed a Linear Regression model using Scikit-learn.

The model was trained using the preprocessed housing dataset.

### Step 8: Model Evaluation

Evaluated the trained model using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

### Step 9: Visualization

Created an Actual vs Predicted House Prices scatter plot to compare the model predictions with actual house prices.

### Step 10: Price Prediction

Used the trained model to predict the price of a new house based on its features.

## 7. Model Performance Results

The Linear Regression model achieved the following results:

| Evaluation Metric | Result |
|---|---:|
| Mean Absolute Error (MAE) | 970,043.40 |
| Mean Squared Error (MSE) | 1,754,318,687,330.66 |
| Root Mean Squared Error (RMSE) | 1,324,506.96 |
| R² Score | 0.6529 |

### Performance Interpretation

- MAE indicates an average absolute prediction error of approximately 970,043 price units.
- RMSE indicates a prediction error of approximately 1,324,507 price units, with larger errors receiving greater weight.
- The R² score of 0.6529 indicates that the model explains approximately 65.29% of the variation in house prices in the test dataset.

The results provide a reasonable baseline for house price prediction using Linear Regression.

## 8. Sample House Price Prediction

Tested the trained model with a new house having the following characteristics:

| Feature | Value |
|---|---:|
| Area | 5000 |
| Bedrooms | 3 |
| Bathrooms | 2 |
| Stories | 2 |
| Main Road | Yes |
| Guest Room | No |
| Basement | No |
| Hot Water Heating | No |
| Air Conditioning | Yes |
| Parking | 2 |
| Preferred Area | Yes |
| Furnishing Status | Semi-furnished |

### Prediction Result

**Predicted House Price: 6,786,094.51**

The model successfully generated a house price prediction using the provided features.

This is an estimated model output and not a guaranteed market price.

## 9. Key Learnings

Through this project, I learned:

- How to load and inspect datasets using Pandas.
- How to perform Exploratory Data Analysis.
- How to visualize data using Matplotlib and Seaborn.
- How to perform correlation analysis.
- How to handle categorical variables.
- How to split data into training and testing sets.
- How to build a Linear Regression model.
- How to evaluate Machine Learning models.
- How to visualize actual and predicted results.
- How to save and reuse a trained Machine Learning model.

## 10. Conclusion

The House Price Prediction project successfully demonstrates the implementation of a Machine Learning regression model using Python and Scikit-learn.

The project covers the complete workflow, including data loading, exploratory data analysis, data preprocessing, correlation analysis, model training, evaluation, visualization, and prediction.

The trained Linear Regression model achieved an R² score of approximately 65.29% on the test dataset.

This project provided practical experience in applying Machine Learning techniques to a real-world prediction problem.

---

**Project Name:** House Price Prediction Using Linear Regression

**Internship:** Oasis Infobyte Data Science Internship

**Programming Language:** Python

**Machine Learning Algorithm:** Linear Regression