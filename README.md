# README



# Real-Time Database Integration and Predictive Maintenance System
# Integrated Leak Detection and Reparation System CodeLeakDetection.py

## Overview

This project simulates an advanced system for integrating real-time sensor data, detecting anomalies in water pipelines, and performing predictive maintenance. The system is designed to:

- Integrate real-time data streams for sound, vibration, and temperature sensors.
- Detect pipeline leaks using anomaly thresholds.
- Adjust water distribution dynamically in response to detected leaks.
- Use predictive analytics to forecast maintenance needs and optimize repair schedules.

**Important**: The current implementation uses a simulated dataset. For real-world deployment, you must replace this with a real-time data source.

## Features

- **Real-Time Data Integration**: Simulated database structure to mimic real-time data handling.
- **Leak Detection**: Identifies anomalies in sensor readings and flags leaks.
- **Dynamic Water Distribution**: Adjusts water flow based on detected leaks.
- **Predictive Maintenance**: Forecasts maintenance requirements using a regression model trained on historical data.

## Prerequisites

- Python 3.8+
- Required libraries:
  - `numpy`
  - `pandas`
  - `scikit-learn`
  - `matplotlib`

Install dependencies using:

```bash
pip install numpy pandas scikit-learn matplotlib
```

## File Structure

- `realtime_database_integration.py`: Main script to simulate real-time database integration and system functionality.
- `README.md`: Documentation file (this document).

## Usage Instructions

### 1. Simulating Real-Time Data

1. Run the main script:
   ```bash
   python CodeLeakDetection.py
   ```
2. The script generates synthetic sensor data and processes it in a simulated real-time database environment.
3. Outputs include:
   - Leak detection summary for each update cycle.
   - Visualizations for predictive maintenance.

### 2. Transition to Real-Time Data

To replace the simulated data with real-time inputs:

1. **Set up a live data source**:

   - Use APIs, IoT devices, or other data streams to provide real-time sensor readings.
   - Ensure data format matches the schema used in the script (`sound`, `vibration`, `temperature`).

2. **Modify the ************************`RealTimeDatabase`************************ class**:
   Replace the `update` method to fetch data from your live source instead of generating simulated data:

   ```python
   def update(self, new_data):
       """Fetch and append live data."""
       live_data = fetch_live_data_source()  # Replace with your data fetching logic
       self.data = pd.concat([self.data, live_data], ignore_index=True)
   ```

3. **Test the integration**:

   - Run the updated script.
   - Verify that live data is processed correctly for leak detection and water distribution adjustments.

### 3. Customization

- Update thresholds for leak detection:
  ```python
  SOUND_THRESHOLD = 70
  VIBRATION_THRESHOLD = 40
  TEMPERATURE_THRESHOLD = 25
  ```
- Adjust regression model parameters for predictive maintenance:
  ```python
  model = LinearRegression()
  model.fit(X, y)
  ```

### 4. Visualizations

The script generates:

- **Leak Detection Logs**: Highlights anomalies and water flow adjustments.
- **Predictive Maintenance Chart**: Visualizes forecasted maintenance needs.



# Water Consumption Thresholds and Incentives for Sustainable Use

# Overview

This initiative promotes sustainalbe water usage by implementing a consumption threshold that leverages real-time data analysis. The code simulates a program that continuously monitors water usage and determines whether it exceeds the set limit. Users who stay within the threshold are rewarded, incentivizing mindful and efficient water consumption. By aligning technology with sustainability, this system aims to reduce waste, foster environmental stewardship, and encourage equitable water usage practices.

**Important**: The current implementation uses a simulated dataset. For real-world deployment, you must replace this with a real-time data source.

## Features

- **Real-Time Data Integration**: Simulated database structure to mimic real-time data handling.
- **Threshold Compliance Analysis**: Compares real-time water usage against predefined thresholds to determine user eligibility for rewards.
- **User Incentive System**: Rewards users who consistently stay within their consumption thresholds, promoting sustainable behavior.
- **Customizable Thresholds**: Adapts consumption limits to regional needs, seasonal variations, or user-specific profiles.

## Prerequisites

- Python 3.8+
- Required libraries:
  - `pandas`
  - `pyarrow`
  - `fastparquet`

Install dependencies using:

```bash
pip install pandas pyarrow fastparquet
```

## File Structure

- `sort_threshold_database_1_no_MySQL.py`: Main script to simulate real-time database integration and system functionality.
- `README.md`: Documentation file (this document).

## Usage Instructions

### 1. Simulating Real-Time Data

1. Run the main script using the following command:
   ```bash
   python sort_threshold_database_1_no_MySQL.py
   ```
2. The script simulates a real-time data environment, processes consumption data, and compares it against set thresholds.
3. Output include:
   - Summary of users meeting or exceeding the thresholds for each update cycle.
   - Incentive eligibility logs for compliant users.

### 2. Customization

- To adjust the consumption thresholds, edit the 'threshold' variable in the script:
  ```python
  threshold = 100.0 # Set the desired threshold value here
  ```
You can further customize thresholds based on user profiles or regional variations within the script.

### 3. Visualization

The script generates:

- **Threshold Logs**: Highlights users who stay within the threshold.
- **Summary Reports**: Aggregated data on compliance and reward distribution.

# Modification of transport on water consumption
# XXXXXXXXXXXXXXXXXXXXXXXX.ipynb



# Anomaly Detection and Public Transport Adjustments (A.D.P.T.A)

## Overview

This project focuses on dynamically detecting anomalies such as heavy rainfall to optimize public transport routes. By leveraging real-time data, the system avoids stops affected by floods, recalculates routes, and ensures safe and efficient transport solutions.

**Important**: While some components use real-world data (e.g., bus stop locations and routes), rainfall data is simulated due to limited access to live datasets. The system is designed to easily integrate real-world data.

## Features

- **Dynamic Route Optimization**: Recalculates bus routes to avoid stops at risk of flooding.
- **Interactive Visualizations**: Compares original and optimized routes on an interactive map.
- **Customizable Thresholds**: Allows users to adjust rainfall thresholds for anomaly detection.
- **Real-Time Adaptability**: Can be connected to live rainfall and route data for deployment.

## Prerequisites

- Python 3.8+
- Required libraries:
  - `pandas`
  - `networkx`
  - `folium`

Install dependencies using:
```bash
pip install -r requirements.txt
```

## File Structure

```
ANOMALY_MODIFICATION_PROJECT/
├── data/                  # Input data files
│   ├── lluvias.csv        # Simulated rainfall intensity data
│   ├── paradas.csv        # H12 bus stop data with coordinates
│   └── rutas.csv          # H12 bus route data
├── outputs/               # Outputs generated by the code
│   ├── rutas_modificadas.csv # Updated bus routes
│   └── visualizacion_rutas.html # Interactive map of the routes
├── src/                   # Source code
│   ├── main.py            # Main script for recalculating routes
│   └── visualizacion.py   # Visualization script for maps
├── .gitignore             # Files to be ignored by Git
├── README.md              # Documentation file (this document)
├── requirements.txt       # Python dependencies
```

## Usage Instructions

### 1. Install Dependencies
Run the following command to install all necessary Python libraries:
```bash
pip install -r requirements.txt
```

### 2. Recalculate Routes
Execute the main script to recalculate bus routes based on simulated rainfall data:
```bash
python src/main.py
```
The recalculated routes will be saved in `outputs/rutas_modificadas.csv`.

### 3. Generate the Visualization
Run the visualization script to create an interactive map:
```bash
python src/visualizacion.py
```
The interactive map will be saved as `outputs/visualizacion_rutas.html`. Open it in your browser to view the results.

## Customization

- **Rainfall Threshold**: Adjust the threshold for heavy rainfall detection in `src/main.py`:
  ```python
  umbral_lluvia = 0.7  # Default threshold for heavy rainfall
  ```
- **Visualization Markers**: Customize the colors and icons for the map markers in `src/visualizacion.py`.

## Results

The system dynamically identifies bus stops affected by heavy rainfall and recalculates routes to avoid them. The interactive map visually compares the original and optimized routes, highlighting safe and efficient transport solutions.




## Contributions

Contributions to make this project fully functional with real-time data are welcome! If you integrate a live data source or enhance any part of the system, please submit a pull request.


## License

This project is open-source and available under the MIT License. This project is submitted as part of the Aigües de Barcelona challenge and is intended for internal use within the scope of the competition. All rights to the project are reserved by the submitting team. The project and its contents are not to be distributed, modified, or used for commercial purposes outside of this challenge without explicit permission from the project team and Aigües de Barcelona.

## Contact
For queries or issues, contact:
- **Raul Andrei Hategan** (Project Manager - PM): [raulandrei.hategan01@estudiant.upf.edu](mailto:raulandrei.hategan01@estudiant.upf.edu)  
- **Sergi Puig i Bertol** (Software & Data Analyst): [sergi.puig04@estudiant.upf.edu](mailto:sergi.puig04@estudiant.upf.edu)  
- **Guillem Pons** (Software Developer & Implementation): [guillem.pons02@estudiant.upf.edu](mailto:guillem.pons02@estudiant.upf.edu)  
- **Pol Brugarolas** (Algorithm Design & Code Implementation): [pol.brugarolas01@estudiant.upf.edu](mailto:pol.brugarolas01@estudiant.upf.edu)  
- **Roger Arola** (Project Documentation & Design): [roger.arola01@estudiant.upf.edu](mailto:roger.arola01@estudiant.upf.edu)  

