import pandas as pd

df = pd.read_csv("dataset/Housing.csv")

# Convert yes/no columns into 1/0
binary_columns = [
    'mainroad',
    'guestroom',
    'basement',
    'hotwaterheating',
    'airconditioning',
    'prefarea'
]

for col in binary_columns:
    df[col] = df[col].map({'yes': 1, 'no': 0})

# Convert furnishing status into numerical columns
df = pd.get_dummies(
    df,
    columns=['furnishingstatus'],
    drop_first=True,
    dtype=int
)

print("PREPROCESSED DATA:")
print(df.head())

print("\nDATA TYPES:")
print(df.dtypes)

# Save processed dataset
df.to_csv("outputs/processed_housing.csv", index=False)

print("\nPreprocessing Completed Successfully!")