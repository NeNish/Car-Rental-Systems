import pandas as pd
import numpy as np
import xgboost as xgb
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error

# Load dataset
df = pd.read_csv('data/car_rental_data.csv')

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Feature Engineering
df['day_of_week'] = df['date'].dt.dayofweek
df['hour'] = df['date'].dt.hour

# One-hot encode categorical variables
df = pd.get_dummies(df, columns=['car_type', 'location'], drop_first=True)

# Normalize numerical data
scaler = StandardScaler()
df[['demand_level', 'competitor_price', 'temperature', 'rainfall']] = scaler.fit_transform(
    df[['demand_level', 'competitor_price', 'temperature', 'rainfall']]
)

# Define Features & Target
X = df.drop(columns=['price'])
y = df['price']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=200)
model.fit(X_train, y_train)

# Evaluate Model
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error: {mae}")

# Save Model
pickle.dump(model, open('models/pricing_model.pkl', 'wb'))
