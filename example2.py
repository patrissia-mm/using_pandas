import pandas as pd
df = pd.read_csv("mod2_Data.csv", na_values=["NaN"])
print(df.head())
print("columnas: ", df.columns)
print("Indice: ", df.index)
""" df.columns = ["titulo", "col1", "col2", "col3"] """
print("VAlues: ", df.values)
print("describe", df.describe())
col1 = df["Alumno;Nota 1;Nota 2;Nota 3"]
print(type(col1))
subset = df.iloc[40:94]
print(subset)
print(df.iloc[:])
