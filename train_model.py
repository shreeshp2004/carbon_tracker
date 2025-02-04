import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflowjs as tfjs

# 📌 Step 1: Dataset - Power Usage (kW) → Carbon Emission (kg CO2 per hour)
data = {
    "power_usage_kW": [0.5, 1.0, 2.0, 3.5, 5.0, 7.0, 10.0, 12.5, 15.0, 20.0],
    "carbon_emission_kg": [0.3, 0.6, 1.2, 2.1, 3.0, 4.2, 6.0, 7.5, 9.0, 12.0]
}

df = pd.DataFrame(data)

# 📌 Step 2: Preprocessing
X = df[["power_usage_kW"]].values
y = df["carbon_emission_kg"].values

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 📌 Step 3: Split Data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 📌 Step 4: Create AI Model
model = keras.Sequential([
    keras.layers.Dense(16, activation="relu", input_shape=(1,)),
    keras.layers.Dense(8, activation="relu"),
    keras.layers.Dense(1)  # Output: Predicted Carbon Emission
])

model.compile(optimizer="adam", loss="mean_squared_error")

# 📌 Step 5: Train the Model
model.fit(X_train, y_train, epochs=100, validation_data=(X_test, y_test))

# 📌 Step 6: Save Model for TensorFlow.js
model.save("carbon_model")
tfjs.converters.save_keras_model(model, "tfjs_model")
