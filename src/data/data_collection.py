import pandas as pd
import numpy as np
import os

from sklearn.model_selection import train_test_split
import yaml

def load_params(file_path : str) -> dict:
    try:
        with open(file_path, 'r') as file:
            params = yaml.safe_load(file)
        return params
    except Exception as e:
        raise Exception(f"Error loading parameters from {file_path}: {e}")


#data = pd.read_csv(r"/Users/parimal/Desktop/PYTHON/PYTHONPRACTICE/PROJECTS/ml_pipeline/original_data/water_potability.csv")

def load_data(file_path: str) -> pd.DataFrame:
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        raise Exception(f"Error loading data from {file_path}: {e}")    


#train_data , test_data = train_test_split(data, test_size=params['data_collection']['test_size'], random_state=42) 
#modular code 

def split_data(data: pd.DataFrame, test_size: float, random_state: int) -> tuple[pd.DataFrame, pd.DataFrame]:
    try:
        train_data, test_data = train_test_split(data, test_size=test_size, random_state=random_state)
        return train_data, test_data
    except Exception as e:
        raise Exception(f"Error splitting data: {e}")

def save_data(train_data: pd.DataFrame, test_data: pd.DataFrame, project_root: str) -> None:
    try:
        data_path = os.path.join(project_root, 'data', 'raw')
        os.makedirs(data_path, exist_ok=True)
        train_data.to_csv(os.path.join(data_path, 'train_data.csv'), index=False)
        test_data.to_csv(os.path.join(data_path, 'test_data.csv'), index=False)
    except Exception as e:
        raise Exception(f"Error saving data: {e}")





def main():
    try:
        # Assuming the script is in 'src', project_root is one level up.
        project_root = os.path.join(os.path.dirname(__file__), '..')
        
        # The params file is inside the src directory
        params = load_params('params.yaml')
        
        original_data_path = os.path.join(project_root, 'original_data', 'water_potability.csv')
        data = load_data(original_data_path)
        
        test_size = params['data_collection']['test_size']
        random_state = params['data_collection']['random_state']
        train_data, test_data = split_data(data, test_size=test_size, random_state=random_state)
        
        save_data(train_data, test_data, project_root)
        print("Data collection, splitting, and saving completed successfully.")
    except Exception as e:
        print(f"Error in data collection process: {e}")    
        
if __name__ == "__main__":
    main()
