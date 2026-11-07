import pandas as pd
import joblib

# Load trained model
model = joblib.load("outputs/house_price_model.pkl")

# New house details
new_house = pd.DataFrame([{
    'area': 5000,
    'bedrooms': 3,
    'bathrooms': 2,
    'stories': 2,
    'mainroad': 1,
    'guestroom': 0,
    'basement': 0,
    'hotwaterheating': 0,
    'airconditioning': 1,
    'parking': 2,
    'prefarea': 1,
    'furnishingstatus_semi-furnished': 1,
    'furnishingstatus_unfurnished': 0
}])

# Predict price
predicted_price = model.predict(new_house)

print("NEW HOUSE DETAILS:")
print(new_house)

print("\nPREDICTED HOUSE PRICE:")
print(predicted_price[0])