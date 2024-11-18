import os
import pandas as pd

def load_datasets(folder_path):
    datasets = {}
    if not os.path.exists(folder_path):
        print(f"Error: La carpeta '{folder_path}' no existe.")
        return datasets

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if filename.endswith('.csv'):
                print(f"Loading CSV dataset: {filename}")
                datasets[filename] = pd.read_csv(file_path, low_memory=False)
            elif filename.endswith('.parquet'):
                print(f"Loading Parquet dataset: {filename}")
                datasets[filename] = pd.read_parquet(file_path)
            elif filename.endswith('.json'):
                print(f"Loading JSON dataset: {filename}")
                datasets[filename] = pd.read_json(file_path)
            else:
                print(f"Skipping file (unsupported format): {filename}")
        except Exception as e:
            print(f"Error loading {filename}: {e}")
    return datasets

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(script_dir, 'datasets')
    datasets = load_datasets(folder_path)

    if not datasets:
        print("No datasets were loaded.")
    else:
        for name, data in datasets.items():
            print(f"\nDataset: {name}")
            print(data.head())

if __name__ == "__main__":
    main()
