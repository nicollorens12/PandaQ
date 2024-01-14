from antlr4 import FileStream, CommonTokenStream
from lcLexer import lcLexer
from lcParser import lcParser
from lcVisitor import lcVisitor
from load_data import load_csv_file
import pandas as pd
import streamlit as st
import os
from lcArbre import lcArbre

# Función para crear o recuperar la instancia de lcArbre desde la caché
@st.cache_resource()
def create_or_get_lcArbre():
    # Cargar los DataFrames desde los archivos CSV
    countries = load_csv_file("countries.csv")
    departments = load_csv_file("departments.csv")
    dependents = load_csv_file("dependents.csv")
    employees = load_csv_file("employees.csv")
    jobs = load_csv_file("jobs.csv")
    locations = load_csv_file("locations.csv")
    regions = load_csv_file("regions.csv")

    # Crear la instancia de lcArbre
    arbol = lcArbre({
        'countries': countries,
        'departments': departments,
        'dependents': dependents,
        'employees': employees,
        'jobs': jobs,
        'locations': locations,
        'regions': regions
    })

    return arbol

# Función principal
def main():
    st.title('PandaQ Nico Llorens')
    st.text('Descripcion')

    # Ingresar la consulta directamente en el script
    sql_query = st.text_area('Query', 'id := SELECT job_id FROM jobs;')

    if st.button('Ejecutar Query'):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        sql_filepath = os.path.join(script_dir, "query.sql")
        with open(sql_filepath, "w") as file:
            file.write(sql_query)

        # Analizar la consulta SQL desde el archivo
        input_stream = FileStream(sql_filepath)
        lexer = lcLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = lcParser(token_stream)
        tree = parser.instruction()

        # Obtener la instancia de lcArbre desde la caché
        arbol = create_or_get_lcArbre()

        # Visitar el árbol y realizar las operaciones
        arbol.visitInstruction(tree)

        st.markdown('### Resultat de la consulta')
        result_df = arbol.get_result()
        st.write(result_df)

if __name__ == '__main__':
    main()

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