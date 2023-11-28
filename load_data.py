# load_data.py
import pandas as pd
import os

def load_csv_file(filename):
    csv_directory = "db"
    filepath = os.path.join(csv_directory, filename)

    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        print(f"El archivo '{filename}' no fue encontrado en '{csv_directory}'.")
        return None
    except pd.errors.EmptyDataError:
        print(f"El archivo '{filename}' está vacío.")
        return None
    except pd.errors.ParserError:
        print(f"Error al analizar el archivo '{filename}'. Asegúrate de que tenga una estructura válida.")
        return None
