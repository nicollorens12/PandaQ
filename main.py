# main.py
from antlr4 import FileStream, CommonTokenStream
from lcLexer import lcLexer
from lcParser import lcParser
from load_data import load_csv_files

def main():
    # Directorio que contiene los archivos CSV (subcarpeta 'db')
    csv_directory = "db"

    # Llamar a la función para cargar los datos desde load_data.py
    database_df = load_csv_files()

    # Imprimir el DataFrame combinado
    print(database_df)

    # Cambia el nombre del archivo SQL según tu estructura
    sql_file = "query.sql"

    # Combinar el directorio y el nombre del archivo SQL
    sql_filepath = os.path.join(csv_directory, sql_file)

    # Analizar la consulta SQL desde el archivo
    input_stream = FileStream(sql_filepath)
    lexer = lcLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = lcParser(token_stream)
    tree = parser.query()

    # Imprimir el árbol de análisis sintáctico (opcional)
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()
