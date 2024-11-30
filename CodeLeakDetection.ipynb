import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import random

# Simulate Real-Time Database Integration
class RealTimeDatabase:
    def __init__(self):
        self.data = pd.DataFrame()

    def update(self, new_data):
        """Simulate updating the database with new real-time data."""
        self.data = pd.concat([self.data, new_data], ignore_index=True)

    def fetch_latest(self):
        """Fetch the latest data entries."""
        return self.data.tail(100)

# Generate Simulated Sensor Data

def generate_sensor_data(n):
    """Generate simulated data for sound, vibration, and temperature."""
    np.random.seed(42)
    sound = np.random.normal(50, 10, n)
    vibration = np.random.normal(30, 5, n)
    temperature = np.random.normal(20, 2, n)

    # Introduce anomalies
    for i in random.sample(range(n), int(n * 0.1)):
        sound[i] += np.random.uniform(20, 50)
        vibration[i] += np.random.uniform(10, 30)
        temperature[i] += np.random.uniform(5, 10)

    return pd.DataFrame({
        'sound': sound,
        'vibration': vibration,
        'temperature': temperature
    })

# Leak Detection

def detect_leaks(data):
    """Detect leaks based on thresholds."""
    leak_indices = data[(data['sound'] > 70) & (data['vibration'] > 40) & (data['temperature'] > 25)].index
    data['leak_detected'] = 0
    data.loc[leak_indices, 'leak_detected'] = 1
    return data

# Adjust Water Distribution

def adjust_water_distribution(data):
    """Simulate water flow adjustments based on leak detection."""
    data['water_flow'] = 100
    data.loc[data['leak_detected'] == 1, 'water_flow'] = 50
    return data

# Predictive Maintenance

def predictive_maintenance(logs):
    """Train a predictive model using maintenance logs."""
    logs['days_since_last_repair'] = (logs['date'] - logs['last_repair']).dt.days
    X = logs[['days_since_last_repair']]
    y = logs['repair_needed']

    model = LinearRegression()
    model.fit(X, y)

    # Predict future maintenance needs
    future_days = np.array([[i] for i in range(0, 365, 30)])
    predictions = model.predict(future_days)

    return future_days.flatten(), predictions

# Main System Simulation
if __name__ == "__main__":
    # Initialize real-time database
    real_time_db = RealTimeDatabase()

    # Simulate periodic updates
    for i in range(10):
        new_data = generate_sensor_data(100)
        real_time_db.update(new_data)

        # Fetch latest data and process it
        latest_data = real_time_db.fetch_latest()
        processed_data = detect_leaks(latest_data)
        processed_data = adjust_water_distribution(processed_data)

        print(f"Update {i + 1}: Leak Detection Summary")
        print(processed_data[processed_data['leak_detected'] == 1])

    # Simulate maintenance logs
    maintenance_logs = pd.DataFrame({
        'date': pd.date_range(start='2023-01-01', periods=10, freq='M'),
        'last_repair': pd.date_range(start='2022-01-01', periods=10, freq='M'),
        'repair_needed': [1, 0, 1, 1, 0, 0, 1, 0, 1, 1]
    })

    # Predict future maintenance needs
    future_days, predictions = predictive_maintenance(maintenance_logs)

    # Visualization
    plt.figure(figsize=(10, 6))
    plt.plot(future_days, predictions, label='Predicted Maintenance Need', marker='o')
    plt.title('Predictive Maintenance Over Time')
    plt.xlabel('Days Since Last Repair')
    plt.ylabel('Maintenance Need (Probability)')
    plt.legend()
    plt.grid()
    plt.show()
