import csv

def read_series(file_path):
    # Abrimos el archivo en modo lectura con soporte para utf-8
    with open(file_path, 'r', encoding='utf-8') as file:
        # DictReader convierte cada fila en un diccionario
        reader = csv.DictReader(file)

        for series in reader:
            # Accedemos a los datos usando los nombres de las columnas como claves
            print(f"Top choice: {series['Name']} on {series['Platform']} - Score: {series['Score']}/10.")

read_series('shows.csv')