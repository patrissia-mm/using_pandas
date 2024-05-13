import pandas as pd
import numpy as np

data = pd.Series([0.25, 0.5, 0.75, 1.0])
"""SEcuencia de valores y de índices"""
print(data)
"""Valores: array NumPy"""
print(data.values)
print(data[1])
print(data[1:3])
"""Construyendo un DataFrame a partir de una lista de diccionarios"""
data2 = [{'a': i, 'b': 2*i} for i in range(3)]
print(pd.DataFrame(data2))
"""Construyendo un Dataframe a partir de una matriz bidimensional de NumPy"""
print(pd.DataFrame(np.random.rand(3, 2), columns=[
      'foo', 'bar'], index=['a', 'b', 'c']))
"""Manejo de índices, nota: son inmutables"""
ind = pd.Index([2,3,5,7,11])
print(ind)
print(ind[1])
print(ind[::2])
indA = pd.Index([1,3,5,7,9])
indB = pd.Index([2,3,5,7,11])
print("Intersection: ", indA & indB)
print("Union: ", indA | indB)
print("Diferencia simétrica: ", indA ^ indB)