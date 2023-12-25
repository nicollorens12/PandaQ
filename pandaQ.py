from antlr4 import FileStream, CommonTokenStream
from lcLexer import lcLexer
from lcParser import lcParser
from lcVisitor import lcVisitor
from load_data import load_csv_file
import pandas as pd
import streamlit as st
import os
from QVisitor import QVisitor

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
    st.title('PandaQ Nico Llorens')
    st.text('Descripcion')

    # Ingresar la consulta directamente en el script
    sql_query = st.text_area('Query', 'q := select first_name,last_name, salary, salary *1.05 as new_salary from employees where department_id=5;')

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
            st.pyplot(result_df.plot.barh(stacked=True).figure)
            arbol.empty_instruction_type()

if __name__ == '__main__':
    main()
