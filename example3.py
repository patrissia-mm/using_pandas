import pandas as pd;

datos_csv = pd.read_csv("datos.csv")
"""Análisis de datos"""
""" print(datos_csv.head())
print(datos_csv.tail())
print(datos_csv.info())
print(datos_csv.describe()) """
"""Limpieza de datos"""
print(datos_csv.info())
#Rellenar los valores nulos con un valor específico o con la media, mediana o moda de la columna
datos_csv.fillna(15,inplace=True)
#Eliminar datos duplicados
datos_csv.drop_duplicates(inplace=True)
#Convertir columnas con tipos de datos incorrectos a tipos de datos adecuados
datos_csv['nota1'] = datos_csv['nota1'].astype('Float64')
#ELiminar o renombrar columnas no relevantes o con nobres ambigüos
datos_csv.drop(['final'], axis=1, inplace=True)
#Aplicar filtros para eliminar registros irrelevantes:
datos_csv = datos_csv[datos_csv['nota1']==10]
#Guardar el DataFrame limpio en un archivo CSV:
datos_csv('nombre_archivo_limpio.csv', index=False)
"""Construir estructuas de datos"""
#Convertir el DataFrame a una lista
data_list = datos_csv.values.tolist()
print(data_list)
#Convertir el DataFrame a una matriz
data_matrix = datos_csv.values
print(data_matrix)