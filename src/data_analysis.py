import pandas as pd

# Load dataset
df = pd.read_csv("dataset/Housing.csv")

# Display first 5 rows
print("FIRST FIVE ROWS:")
print(df.head())

# Dataset shape
print("\nDATASET SHAPE:")
print(df.shape)

# Column names
print("\nCOLUMN NAMES:")
print(df.columns.tolist())

# Dataset information
print("\nDATASET INFORMATION:")
print(df.info())

# Missing values
print("\nMISSING VALUES:")
print(df.isnull().sum())