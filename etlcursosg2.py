import numpy as np
import pandas as pd

ventas = pd.read_csv('ventascursos.csv')
print(ventas.head())
print(ventas.info)
print(ventas.describe())
print("-----------------identificacion de nulos ----------------------")
print(ventas.isnull().sum())

print("-----------estandarización de nombres de columnas-----------------")
columnas = ["id_cliente","nombre_cliente","ciudad","id_curso","curso","modalidad","instructor","monto"]
for col in columnas:
    ventas[col]=(ventas[col].astype(str).str.strip())

    ventas["nombre_cliente"] = ventas["nombre_cliente"].str.lower().str.title()
    print("clientes limpios")
    print(ventas["nombre_cliente"].unique())
    print("----------Estandarización de cursos ------------------")
    print(ventas["curso"].unique())

    ventas["curso"] = ventas["curso"].str.lower().str.title()
    print("-------------- cursos limpios -------------------")
    print(ventas["curso"].unique())

    ventas["curso"] = (ventas["curso"].replace({"Powerbi": "Power Bi"}))
    print(ventas["curso"].unique())

    print("----------Estandarización de modalidades ------------------")
    print(ventas["modalidad"].unique())
    ventas["modalidad"] = ventas["modalidad"].str.lower().str.title()
    print("------------- modalidades limpias ------------------")
    print(ventas["modalidad"].unique())

    #Estandarizacion de cuidades 
    print("----------Estandarización de ciudades ------------------")
    print(ventas["ciudad"].unique())

    ventas["ciudad"] = (ventas["ciudad"].replace({"CDMX": "Ciudad de Mexico","QRO": "Queretaro"}))
    ventas["ciudad"] = ventas["ciudad"].str.lower().str.title()
    print("------------- ciudades limpias ------------------")
    print(ventas["ciudad"].unique())


    print("----------Estandarización de instructores ------------------")
    print(ventas["instructor"].unique())

    print("------------- instructores limpios ------------------")
    ventas["instructor"] = (ventas["instructor"].replace({"dr ramirez": "Dr. Ramirez", "DRA LOPEZ": "Dra. Lopez", "ing torres" : "Ing. Torres"}))
    ventas["instructor"] = ventas["instructor"].str.lower().str.title()
print(ventas["instructor"].unique())


print("------------- monto ------------------")
ventas["monto"] = ventas["monto"].astype(str).str.replace("$","",regex=False).str.strip()
ventas["monto"]= pd.to_numeric(ventas["monto"], errors="coerce")# Forz el cambio a numérico
print(ventas["monto"].isnull().sum())

montoprom = ventas['monto'].mean() #obtiene promedio de monto
ventas["monto"] = ventas["monto"].fillna(montoprom)# rellena los nulos con el promedio
print(ventas["monto"].isnull().sum())

#convertir a formato fecha
print("----------------- fechas -----------------------")
ventas["fecha"] = pd.to_datetime(ventas["fecha"], errors="coerce")
print(ventas["fecha"].isnull().sum())

print("------------- eliminar duplicados ------------------")
print(ventas.duplicated().sum()) #cuenta los dusplicados 
ventas = ventas.drop_duplicates()#elimina los duplicados

print(len(ventas))
print(ventas.duplicated().sum())#selecciona los duplicsdos 

print(ventas.info())

print(ventas.shape)

ventas.to_csv("ventascursos_limpias.csv", index=False)