
# Anomaly Detection and Public Transport Adjustments (A.D.P.T.A)

This project implements algorithms to optimize public transport routes in response to anomalies like heavy rainfall and integrates solutions for effective water management.

## How to Run the Project

1. **Install Dependencies**:
   Run the following command to install required packages:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Main Script**:
   Generate modified routes by running:
   ```bash
   python src/main.py
   ```

3. **Visualize the Results**:
   Create an interactive map:
   ```bash
   python src/visualizacion.py
   ```
   Open `outputs/visualizacion_rutas.html` in a browser to see the results.

## Data Files

- `lluvias.csv`: Simulated rainfall data for bus stops.
- `paradas.csv`: Real-world data for H12 bus stops in Barcelona, including latitude and longitude.
- `rutas.csv`: Real-world bus route data for the H12 line.

## Results

The solution dynamically calculates new bus routes based on rainfall intensity, avoiding stops at risk of flooding while minimizing travel time. An interactive map is provided to visualize the original and modified routes.

## Dependencies

See `requirements.txt` for all Python dependencies.

## License

This project is for educational purposes and does not currently use real-time public transport or rainfall data for production environments.
