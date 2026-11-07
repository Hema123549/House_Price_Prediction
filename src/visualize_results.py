import pandas as pd
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split

# Load dataset and trained model
df = pd.read_csv("outputs/processed_housing.csv")
model = joblib.load("outputs/house_price_model.pkl")

# Separate features and target
X = df.drop("price", axis=1)
y = df["price"]

# Use the same train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Predict house prices
y_pred = model.predict(X_test)

# Actual vs Predicted plot
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred)
plt.xlabel("Actual House Prices")
plt.ylabel("Predicted House Prices")
plt.title("Actual vs Predicted House Prices")

# Reference line
min_price = min(y_test.min(), y_pred.min())
max_price = max(y_test.max(), y_pred.max())
plt.plot([min_price, max_price],
         [min_price, max_price], 'r--')

plt.tight_layout()
plt.savefig("outputs/actual_vs_predicted.png")
plt.show()

print("Visualization Completed Successfully!")