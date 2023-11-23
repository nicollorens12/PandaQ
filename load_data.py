# load_data.py
import pandas as pd
import os

def load_csv_files():
    csv_directory = "db"
    dataframes = []
    for filename in os.listdir(csv_directory):
        if filename.endswith(".csv"):
            filepath = os.path.join(csv_directory, filename)
            df = pd.read_csv(filepath)
            dataframes.append(df)
    combined_df = pd.concat(dataframes, ignore_index=True)
    return combined_df
# load_data.py
import pandas as pd
import os

def load_csv_files():
    csv_directory = "db"
    dataframes = []
    for filename in os.listdir(csv_directory):
        if filename.endswith(".csv"):
            filepath = os.path.join(csv_directory, filename)
            df = pd.read_csv(filepath)
            dataframes.append(df)
            
            try:
                df = pd.read_csv(filepath)
                dataframes.append(df)
            except pd.errors.ParserError as e:
                print(f"Error en el archivo {filename}: {e}")
    combined_df = pd.concat(dataframes, ignore_index=True)
    return combined_df
