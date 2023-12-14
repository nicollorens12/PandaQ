from antlr4 import FileStream, CommonTokenStream
from lcLexer import lcLexer
from lcParser import lcParser
from lcVisitor import lcVisitor
from load_data import load_csv_file
import pandas as pd
import streamlit as st
import os
from lcArbre import lcArbre



# Cargar los DataFrames desde los archivos CSV
countries = load_csv_file("countries.csv")
departments = load_csv_file("departments.csv")
dependents = load_csv_file("dependents.csv")
employees = load_csv_file("employees.csv")
jobs = load_csv_file("jobs.csv")
locations = load_csv_file("locations.csv")
regions = load_csv_file("regions.csv")

# Función principal
def main():
    st.title('PandaQ Nico Llorens')
    st.text('Descripcion')
    #st.markdown('## Titulo 2')
    
    # Ingresar la consulta directamente en el script
    #sql_file = "query.sql"
    
    sql_query = st.text_area('Query', 'SELECT first_name,salary,salary * 1.05 AS new_salary FROM employees;')
    # Imprimir la consulta
    #print("Consulta ingresada:", sql_query)
    
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
        tree = parser.query()

        #   Crear un objeto Visitor y visitar el árbol
        arbol = lcArbre({
            'countries': countries,
            'departments': departments,
            'dependents': dependents,
            'employees': employees,
            'jobs': jobs,
            'locations': locations,
            'regions': regions
        })
        arbol.visit(tree)

        arbol.printResult()
        st.markdown('### Resultat de la consulta')
        result_df = arbol.get_result()
        st.write(result_df)
        
if __name__ == '__main__':
    main()
