## UPFH2O

# CodeLeakDetection.ipynb
# Integrated Leak Detection and Reparation System

## Overview
This project simulates a comprehensive system for detecting water pipeline leaks, adjusting water distribution in real time, and performing predictive maintenance based on historical data. The system integrates:

- Advanced leak detection using sensor data (ground sound, vibration, and temperature).
- Proportional water distribution adjustments to optimize resource use.
- Predictive analytics using a linear regression model to forecast maintenance needs.

## Features
- **Leak Detection**: Identifies anomalies in sensor data and flags potential leaks.
- **Dynamic Water Distribution**: Automatically adjusts water flow in affected areas.
- **Predictive Maintenance**: Uses machine learning to anticipate future maintenance requirements.

## Prerequisites
- Python 3.8+
- Required libraries:
  - `numpy`
  - `pandas`
  - `sklearn`
  - `matplotlib`

Install dependencies using:
```bash
pip install numpy pandas scikit-learn matplotlib
```

## File Structure
- `leak_detection_simulation.py`: Main script to simulate the leak detection and repair system.
- `sensor_data.csv`: Sample data for sensor readings (ground sound, vibration, temperature).
- `maintenance_history.csv`: Historical maintenance records for predictive analytics.
- `README.md`: User manual.

## Usage Instructions
### 1. Running the Simulation
1. Ensure all required files are in the working directory.
2. Execute the script:
   ```bash
   python leak_detection_simulation.py
   ```
3. The script performs the following:
   - Simulates sensor data and detects anomalies.
   - Adjusts water flow dynamically for flagged regions.
   - Runs predictive maintenance analysis and outputs a timeline for required repairs.

### 2. Input Files
- **`sensor_data.csv`**:
  - Columns:
    - `Region`: Identifier for the region.
    - `GroundSound`: Measured sound levels.
    - `Vibration`: Measured vibration levels.
    - `Temperature`: Measured ground temperature.
  - Example:
    ```csv
    Region,GroundSound,Vibration,Temperature
    A,20,15,30
    B,50,45,80
    C,25,20,40
    ```

- **`maintenance_history.csv`**:
  - Columns:
    - `Region`: Identifier for the region.
    - `LastMaintenance`: Days since last maintenance.
    - `LeakReports`: Number of reported leaks.
    - `PipeAge`: Age of the pipeline in years.
  - Example:
    ```csv
    Region,LastMaintenance,LeakReports,PipeAge
    A,180,2,10
    B,300,5,15
    C,90,1,5
    ```

### 3. Output
- **Leak Detection**:
  - Prints a list of regions with potential leaks.
  - Saves adjusted water flow information to `adjusted_flow.csv`.

- **Predictive Maintenance**:
  - Displays a bar chart of predicted maintenance needs.
  - Saves predictions to `maintenance_predictions.csv`.

### 4. Customization
- Update sensor thresholds in the script to match real-world values:
  ```python
  SOUND_THRESHOLD = 30
  VIBRATION_THRESHOLD = 20
  TEMPERATURE_THRESHOLD = 50
  ```

- Modify regression model parameters for predictive maintenance in the script:
  ```python
  model = LinearRegression()
  model.fit(X, y)
  ```

### 5. Visualizations
- The script generates:
  - **Leak detection logs**: Highlighted anomalies.
  - **Predictive maintenance chart**: Forecasted maintenance needs based on pipeline conditions.

## Best Practices
- Ensure timely updates to `sensor_data.csv` and `maintenance_history.csv` for accuracy.
- Regularly retrain the predictive model with updated maintenance records.
- Fine-tune thresholds and regression parameters to align with environmental changes.

## Troubleshooting
- **No anomalies detected**:
  - Verify `sensor_data.csv` for realistic values.
  - Adjust anomaly thresholds.

- **Inaccurate maintenance predictions**:
  - Ensure `maintenance_history.csv` includes diverse and comprehensive data.
  - Experiment with additional features (e.g., material type, water pressure).

## Contact
For queries or issues, contact:
- **Raul Andrei Hategan**: [raulandrei.hategan01@estudiant.upf.edu](mailto:raulandrei.hategan01@estudiant.upf.edu)
