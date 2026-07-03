import pandas as pd 

# se carga el csv de las consultas
consultas = pd.read_csv("consultasmedicassucio.csv")

print('--------Cabezaras--------')
print(consultas.head())
print('-------tipos de datos--------')
print(consultas.info())
print('-------estadisticas--------')
print(consultas.describe())

print('-------valores nulos--------')
#cuenta los valores nulos por columna
print(consultas.isnull().sum())

print ('-------duplicados--------')
#cuenta los registros duplicados
print(consultas.duplicated().sum())
# se dectectan 5 valores duplicados, se eliminan
consultas = consultas.drop_duplicates()
print(consultas.duplicated().sum())# se confirma que ya no hay duplicados

# se estandarisa el nombre de los campos 
columnas = ["id_paciente","paciente","id_especialidad","especialidad","medico","ciudad","tipo_consulta","fecha","costo"]
for col in columnas:
    consultas[col] = (consultas[col].astype(str).str.strip())

print("-------------estandarización de nombres de pacientes------------------")
#trae el nombre de los pacientes y los estandariza
print(consultas["paciente"].unique())#muestra los nombres
consultas["paciente"] = consultas["paciente"].str.lower().str.title()#los estandariza
print('--------comprobación de corrección----------')
print(consultas["paciente"].unique())
print(consultas["id_paciente"].unique())#muestra los id de pacientes

print('---------estandarizacion de especialidades-----------')
print(consultas["especialidad"].unique())#muestra las especialidades
print(consultas["id_especialidad"].unique())#muestra los id de especialidades

print('---------estandarizacion de medicos-----------')
print(consultas["medico"].unique())#muestra los medicos
#se detecta nombres de medicos con errores de tipeo, se corrigen
consultas["medico"] = (consultas["medico"].replace({"dr garcia": "Dr Garcia", "dra lopez": "Dra Lopez", "dra torres" : "Dra Torres", "dr ramirez": "Dr Ramirez", "dr perez": "Dr Perez"}))
consultas["medico"] = consultas["medico"].str.lower().str.title()#se estandarizan los nombres de los medicos
print(consultas["medico"].unique())#muestra los medicos corregidos

print('---------estandarizacion de ciudades-----------')
print(consultas["ciudad"].unique())#muestra las ciudades
#se detecta nombres de ciudades con errores de tipeo, se corrigen
consultas["ciudad"] = (consultas["ciudad"].replace({"cdmx": "Ciudad de Mexico","CDMX": "Ciudad de Mexico", "qro": "Queretaro", "QRO": "Queretaro","GDL": "Guadalajara"}))
consultas["ciudad"] = consultas["ciudad"].str.lower().str.title()#se estandarizan los nombres de las ciudades
print(consultas["ciudad"].unique())#muestra las ciudades corregidas

print('---------estandarizacion de tipo de consulta-----------')
print(consultas["tipo_consulta"].unique())#muestra los tipos de consulta
consultas["tipo_consulta"] = consultas["tipo_consulta"].str.lower().str.title()#se estandarizan los nombres de los tipos de consulta
print(consultas["tipo_consulta"].unique())#muestra los tipos de consulta corregidos

print('---------estandarizacion de fecha-----------')
#se convierte la columna fecha a tipo datetime
consultas["fecha"] = pd.to_datetime(consultas["fecha"], errors="coerce")
print(consultas["fecha"].isnull().sum())#cuenta los valores nulos en la columna fecha
print(consultas["fecha"].dtype)#muestra el tipo de dato de la columna fecha

print('---------estandarizacion de costo-----------')
#se elimina el simbolo de pesos y se convierte a tipo numerico
print(consultas["costo"].unique())#muestra los costos
print(consultas["costo"].isnull().sum())#cuenta los valores nulos en la columna costo
print(consultas["costo"].dtype)#muestra el tipo de dato de la columna costo
consultas["costo"] = pd.to_numeric(consultas["costo"].str.replace("$","",regex=False).str.strip(), errors="coerce")#se elimina el simbolo de pesos y se convierte a tipo numerico
print(consultas["costo"].unique())#comprobacion de los costos corregidos

print(len(consultas))#muestra el numero de registros despues de la limpieza
print(consultas.duplicated().sum())#muestra el numero de registros duplicados

print(consultas.shape)

consultas.to_csv("consultasmedicaslimpio.csv", index=False)

