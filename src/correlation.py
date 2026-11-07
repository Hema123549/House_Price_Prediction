import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("dataset/Housing.csv")

# Convert categorical columns into numerical values
df_encoded = pd.get_dummies(df, drop_first=True, dtype=int)

# Calculate correlation
correlation = df_encoded.corr()

# Display correlation with price
print("\nCORRELATION WITH HOUSE PRICE:")
print(correlation['price'].sort_values(ascending=False))

# Create heatmap
plt.figure(figsize=(12, 8))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("House Price Correlation Heatmap")
plt.tight_layout()

plt.savefig("outputs/correlation_heatmap.png")

plt.show()

print("\nCorrelation Analysis Completed!")