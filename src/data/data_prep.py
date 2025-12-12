# src/data_prep.py
from pathlib import Path
import pandas as pd

# --- Paths: resolve from project root (parent of src/data) ---
ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = ROOT / "data" / "raw"
PROC_DIR = ROOT / "data" / "processed"
PROC_DIR.mkdir(parents=True, exist_ok=True)

# --- Read input splits ---
#train_data = pd.read_csv(RAW_DIR / "train_data.csv")
#test_data  = pd.read_csv(RAW_DIR / "test_data.csv")

def load_data(file_path: Path) -> pd.DataFrame:
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        raise Exception(f"Error loading data from {file_path}: {e}")




# --- Utilities (no chained assignment) ---
def fill_missing_with_median(df: pd.DataFrame) -> pd.DataFrame:
    try:
        # compute medians only for numeric columnss
            #medians = df.select_dtypes(include="number").median()
            mean_value = df.select_dtypes(include="number").mean()
            # return a new frame with NA filled (no inplace, avoids FutureWarning)
            return df.copy().fillna(mean_value)
    except Exception as e:
        raise Exception(f"Error filling missing values: {e}")

# --- Process ---
#train_processed = fill_missing_with_median(train_data)
#test_processed  = fill_missing_with_median(test_data)

def save_data(df, file_path: Path) -> None:
    try:
        df.to_csv(file_path, index=False)
    except Exception as e:
        raise Exception(f"Error saving data to {file_path}: {e}")






def main():
    try:
        # Load data
        train_data = load_data(RAW_DIR / "train_data.csv")
        test_data  = load_data(RAW_DIR / "test_data.csv")
        
        # Process data
        train_processed = fill_missing_with_median(train_data)
        test_processed  = fill_missing_with_median(test_data)
        
        # Save processed data
        save_data(train_processed, PROC_DIR / "train_processed.csv")
        save_data(test_processed, PROC_DIR / "test_processed.csv")
        print("Data preparation completed successfully.")
    except Exception as e:
        print(f"Error in data preparation: {e}")



if __name__ == "__main__":
    main()
