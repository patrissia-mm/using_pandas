import pandas as pd;
import matplotlib.pyplot as plt
import scipy.stats as sc
import numpy as np

datos = pd.read_excel("matematicas.xlsx",sheet_name='Hoja1', header=0)
"""Análisis de datos"""
""" print(datos.head())
print(datos.tail())
print(datos.info())
print(datos.describe()) """
"""Limpieza de datos"""
""" print(datos.info())
#Rellenar los valores nulos con un valor específico o con la media, mediana o moda de la columna
datos.fillna(15,inplace=True)
#Eliminar datos duplicados
datos_csv.drop_duplicates(inplace=True)
#Convertir columnas con tipos de datos incorrectos a tipos de datos adecuados
datos_csv['nota1'] = datos_csv['nota1'].astype('Float64')
#ELiminar o renombrar columnas no relevantes o con nobres ambigüos
datos_csv.drop(['final'], axis=1, inplace=True)
#Aplicar filtros para eliminar registros irrelevantes:
datos_csv = datos_csv[datos_csv['nota1']==10]
#Guardar el DataFrame limpio en un archivo CSV:
datos_csv('nombre_archivo_limpio.csv', index=False) """
"""Construir estructuras de datos"""
#Convertir el DataFrame a una lista
""" data_list = datos_csv.values.tolist()
print(data_list)
#Convertir el DataFrame a una matriz
data_matrix = datos_csv.values
print(data_matrix) """

"""Nota máxima"""
""" maximas = ['Notas maximas', datos['Nota1'].max(), datos['Nota2'].max(), datos['Nota3'].max()]
print(maximas)
ultimaFila = len(datos)
print(ultimaFila)
datos.loc[ultimaFila] = maximas """

"""Calcular la media"""
media = datos['Nota1'].mean()
print("Media: ", media)

"""Calcular la varianza"""
nota1 = datos['Nota1']
varianza = nota1.var()
print("Varianza: ", varianza)

"""Calcular la medaina"""
mediana = datos['Nota1'].median()
print("Mediana: ", mediana)

"""Quantiles """
q25 =datos['Nota1'].quantile(0.25)
print("Quantil 25", q25)
cuantiles = datos['Nota1'].quantile([0.25,0.5,0.75])
print("Cuantiles: ", cuantiles)

"""Gráfico con la distribución normal"""
values = datos['Nota1']
mean = values.mean()
std = values.std()
distribution = sc.norm(mean,std)
x=np.linspace(values.min(), values.max(),100)
pdf = distribution.pdf(x)
cdf = distribution.cdf(x)

plt.plot(x,pdf,label="Distribución normal")
values.plot.hist(density=True, alpha=0.5, label="Datos originales")
plt.legend()
plt.show()
"""Crear un histograma"""
""" plt.hist(datos['Nota1'])
plt.show() """

"""Crear un scatterplot"""
""" plt.scatter(datos['Nota1'],datos['Alumno'])
plt.show() """