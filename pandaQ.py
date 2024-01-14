from antlr4 import FileStream, CommonTokenStream
from lcLexer import lcLexer
from lcParser import lcParser
from lcVisitor import lcVisitor
import pandas as pd
import streamlit as st
import os
from QVisitor import QVisitor
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


# Función para crear o recuperar la instancia de QVisitor desde la caché
@st.cache_resource()
def create_or_get_QVisitor():
    # Cargar los DataFrames desde los archivos CSV
    countries = load_csv_file("countries.csv")
    departments = load_csv_file("departments.csv")
    dependents = load_csv_file("dependents.csv")
    employees = load_csv_file("employees.csv")
    jobs = load_csv_file("jobs.csv")
    locations = load_csv_file("locations.csv")
    regions = load_csv_file("regions.csv")

    # Crear la instancia de QVisitor
    arbol = QVisitor({
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
    st.markdown("""## PandaQ Nico Llorens\nIngrese una consulta SQL en el cuadro de texto y presione el botón "Ejecutar Query" para obtener el resultado.\n\nAdemas, puede guardar consultas como tablas nuevas haciendo ```nombreTablaNueva := consulta;```.\n\nTambién puede hacer un gráfico (solo de los terminos númericos de la tabla) haciendo ```plot nombreTabla;```.\n\nTodas las instrucciones deben acabar con un ;.""")

    # Consulta SQL por defecto (ejemplo)
    sql_query = st.text_area('Query', 'select employee_id, first_name, last_name from employees where department_id in (select department_id from departments where location_id = 1700) order by first_name, last_name;')

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

        # Obtener la instancia de QVisitor desde la caché
        arbol = create_or_get_QVisitor()

        # Visitar el árbol y realizar las operaciones
        arbol.visitInstruction(tree)
        result_df = arbol.get_result()
        if arbol.instruction_type == "assignment" or arbol.instruction_type == "query":
            st.write(result_df)
            arbol.empty_instruction_type()
        elif arbol.instruction_type == "plot":
            st.line_chart(result_df)
            arbol.empty_instruction_type()

if __name__ == '__main__':
    main()
