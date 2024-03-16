import json
import pandas as pd
# install openpyxl pip install openpyxl
import random

# Abrir el archivo JSON
with open('files/config_file.json', 'r') as archivo:
    # Leer el contenido del archivo JSON
    datos = json.load(archivo)

# Ahora `datos` contiene la información del archivo JSON
total_records = datos['records_per_arc']
casos = datos['cases']

def obtener_distribucion(casos, tipo_caso):
    for caso in casos:
        if caso['case_id'] == tipo_caso:
            return caso['distribution']

def obtener_distribucion_subcaso(casos, tipo_caso, tipo_subcaso):
    for caso in casos:
        if caso['case_id'] == tipo_caso:
            for subcasos in caso['sub_cases']:
                if subcasos['case_id'] == tipo_subcaso:
                    return subcasos['distribution']

def cantidad_records_subtipo(casos, tipo, subtipo):
    """ Obtener la cantidad de records por subtipo"""

    distribucion = obtener_distribucion(casos, tipo)
    total_records_distribucion = (total_records * distribucion)
    total_records_distribucio_subtipo = obtener_distribucion_subcaso(casos, tipo, subtipo)
    return total_records_distribucion * total_records_distribucio_subtipo


# DATOS SIMILAR
total_records_similar_same = cantidad_records_subtipo(casos, 'SIMILAR', 'SAME')
total_records_similar_typo = cantidad_records_subtipo(casos, 'SIMILAR', 'TYPO')
print(f"SAME: {total_records_similar_same}")
print(f"TYPO: {total_records_similar_typo}")

# DATOS FAMILY
total_records_family_parent_child = cantidad_records_subtipo(casos, 'FAMILY', 'PARENT_CHILD')
total_records_family_twin = cantidad_records_subtipo(casos, 'FAMILY', 'TWINS')
total_records_family_sibling = cantidad_records_subtipo(casos, 'FAMILY', 'SIBLINGS')
print(f"PARENT_CHILD: {total_records_family_parent_child}")
print(f"TWINS: {total_records_family_twin}")
print(f"SIBLINGS: {total_records_family_sibling}")

# DATOS LOW SIMILARITY
total_records_low_similarity_NOMATCH_FN_DOB = cantidad_records_subtipo(casos, 'LOW_SIMILARITY', 'NOMATCH_FN_DOB')
total_records_low_similarity_NOMATCH_LN_DOB = cantidad_records_subtipo(casos, 'LOW_SIMILARITY', 'NOMATCH_LN_DOB')
total_records_low_similarity_NOMATCH_SSN = cantidad_records_subtipo(casos, 'LOW_SIMILARITY', 'NOMATCH_SSN')
total_records_low_similarity_NOMATCH_DOB_ZIP = cantidad_records_subtipo(casos, 'LOW_SIMILARITY', 'NOMATCH_DOB_ZIP')
print(f"NOMATCH_FN_DOB: {total_records_low_similarity_NOMATCH_FN_DOB}")
print(f"NOMATCH_LN_DOB: {total_records_low_similarity_NOMATCH_LN_DOB}")
print(f"NOMATCH_SSN: {total_records_low_similarity_NOMATCH_SSN}")
print(f"NOMATCH_DOB_ZIP: {total_records_low_similarity_NOMATCH_DOB_ZIP}")

# Leer el archivo Excel
datos_excel = pd.read_excel('files/Hackathon-Information.xlsx')

# Imprimir la primera fila
indice = datos_excel.iloc[1]
num_random = random.randint(2, 26)
fila_random = datos_excel.iloc[num_random]

# Luego, convertimos esta lista de tuplas en un diccionario
semilla_dictionario = dict(zip(indice, fila_random))

# Crear un DataFrame de la semilla
semilla_df = pd.DataFrame(semilla_dictionario, index=[0])

# EMPEZAR A ITERAR
from similar import same, typo
from family import parent_child
# SAME
lista_same = []
for _ in range(int(total_records_similar_same)):
    record = same(semilla_dictionario)
    lista_same.append(record)
    
for _ in range(1):             #range(int(total_records_family_parent_child)):
    record = parent_child(semilla_dictionario)
    lista_same.append(record)

# TYPO
# lista_typo = []

# for _ in range(int(total_records_similar_typo)):
#     record = typo(semilla_dictionario)
#     lista_same.append(record)

# Convertir las filas adicionales a DataFrame de Pandas
nuevas_filas_df = pd.DataFrame(lista_same)

# Concatenar el DataFrame original con el DataFrame de filas adicionales
semilla_df = pd.concat([semilla_df, nuevas_filas_df], ignore_index=True)

# Especificar la ruta y nombre del archivo Excel
nombre_archivo = 'resultado.xlsx'

# Escribir el DataFrame en el archivo Excel
semilla_df.to_excel(nombre_archivo, index=False)

print("Nuevas filas agregadas exitosamente al archivo Excel.")
