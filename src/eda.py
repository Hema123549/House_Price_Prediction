import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("dataset/Housing.csv")

# Set visualization style
sns.set_style("whitegrid")

# 1. House Price Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['price'], kde=True)
plt.title("Distribution of House Prices")
plt.xlabel("House Price")
plt.ylabel("Frequency")
plt.savefig("outputs/price_distribution.png")
plt.show()

# 2. Area vs Price
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='area', y='price')
plt.title("Area vs House Price")
plt.savefig("outputs/area_vs_price.png")
plt.show()

# 3. Bedrooms vs Price
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='bedrooms', y='price')
plt.title("Bedrooms vs House Price")
plt.savefig("outputs/bedrooms_vs_price.png")
plt.show()

# 4. Furnishing Status vs Price
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='furnishingstatus', y='price')
plt.title("Furnishing Status vs House Price")
plt.savefig("outputs/furnishing_vs_price.png")
plt.show()

print("EDA Completed Successfully!")