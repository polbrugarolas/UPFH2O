import os
import pandas as pd

def load_datasets(folder_path):
    datasets = {}
    # Verificar si la carpeta existe
    if not os.path.exists(folder_path):
        print(f"Error: La carpeta '{folder_path}' no existe.")
        return datasets

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        # Verificar que sea un archivo CSV
        if filename.endswith('.csv'):
            print(f"Loading dataset: {filename}")
            datasets[filename] = pd.read_csv(file_path)
        else:
            print(f"Skipping file (not a CSV): {filename}")
    return datasets

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(script_dir, 'datasets')
    datasets = load_datasets(folder_path)

    # Verificar si se cargaron datasets
    if not datasets:
        print("No datasets were loaded.")
    else:
        # Muestra un ejemplo de cada dataset cargado
        for name, data in datasets.items():
            print(f"\nDataset: {name}")
            print(data.head())  # Muestra las primeras filas del dataset


if __name__ == "__main__":
    main()

