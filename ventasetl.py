import pandas as pd
from sqlalchemy import create_engine

#crear conexion de base de datos 

engine = create_engine("mssql+pyodbc://sa:Admsis123@localhost:1433/startmodelg2?driver=ODBC+Driver+17+for+SQL+Server")
print (pd.read_sql("SELECT DB_NAME() as bd",engine))

ventas = pd.read_csv("ventascursos_limpias.csv")
ventas['fecha']=pd.to_datetime(ventas["fecha"]).dt.date

ventas["cantidadVentas"]=1

dimcurso = ventas[["id_curso", "curso"]]
dimcurso = dimcurso.drop_duplicates()
dimcurso.to_sql("dimCurso", engine, if_exists="append", index=False)
print("Dimensión Curso cargada")

#Dim instructor
diminstructor = ventas[["instructor"]]
diminstructor = diminstructor.drop_duplicates()
diminstructor.to_sql("dimInstructor", engine, if_exists="append", index=False)
print("Dimensión Instructor cargada")

#Dim modalidad
dimmodalidad = ventas[["modalidad"]]
dimmodalidad = dimmodalidad.drop_duplicates()
dimmodalidad.to_sql("dimModalidad", engine, if_exists="append", index=False)
print("Dimensión Modalidad cargada")

#Dim ciudad
dimciudad = ventas[["ciudad"]]
dimciudad = dimciudad.drop_duplicates()
dimciudad.to_sql("dimCiudad", engine, if_exists="append", index=False)
print("Dimensión Ciudad cargada")


#Dim cliente 
dimcliente = ventas[["id_cliente", "nombre_cliente"]]
dimcliente = dimcliente.drop_duplicates()
dimcliente.to_sql("dimCliente", engine, if_exists="append", index=False)
print("Dimensión Cliente cargada")

#dim tiempo 
dimtiempo = pd.DataFrame()
dimtiempo["fecha"] = ventas[["fecha"]]
dimtiempo["dia"] = pd.to_datetime(dimtiempo["fecha"]).dt.day
dimtiempo["mes"] = pd.to_datetime(dimtiempo["fecha"]).dt.month
dimtiempo["anio"] = pd.to_datetime(dimtiempo["fecha"]).dt.year
dimtiempo = dimtiempo.drop_duplicates()
dimtiempo.to_sql("dimTiempo", engine, if_exists="append", index=False)
print("Dimensión Tiempo cargada")

#Leer dimenciones de SQL 
dimcurso_sql = pd.read_sql("SELECT * FROM dimCurso", engine)
dimcliente_sql = pd.read_sql("SELECT * FROM dimCliente", engine)
diminstructor_sql = pd.read_sql("SELECT * FROM dimInstructor", engine)  
dimmodalidad_sql = pd.read_sql("SELECT * FROM dimModalidad", engine)
dimciudad_sql = pd.read_sql("SELECT * FROM dimCiudad", engine)
dimtiempo_sql = pd.read_sql("SELECT * FROM dimTiempo", engine)
dimtiempo_sql["fecha"] = pd.to_datetime(dimtiempo_sql["fecha"]).dt.date

factventas= ventas.copy()
#fact cursos
factventas = factventas.merge(dimcurso_sql[['dimcursoSK','id_curso']], on="id_curso", how="left")
#fact instructor    
factventas = factventas.merge(diminstructor_sql[['diminstructorSK','instructor']], on="instructor", how="left")
#fact modalidad
factventas = factventas.merge(dimciudad_sql[['dimciudadSK','ciudad']], on="ciudad", how="left")
#fact cliente
factventas = factventas.merge(dimcliente_sql[['dimclienteSK','id_cliente']], on="id_cliente", how="left")
#fact ciudad
factventas = factventas.merge(dimmodalidad_sql[['dimmodalidadSK','modalidad']], on="modalidad", how="left")
#fact tiempo
factventas = factventas.merge(dimtiempo_sql[['dimtiempoSK','fecha']], on="fecha", how="left")

#cargar tabla de hechos
factventas = factventas[["dimcursoSK", "diminstructorSK", "dimciudadSK","dimtiempoSK","dimclienteSK","dimmodalidadSK","monto","cantidadVentas"]]
factventas.to_sql("FactVentas", engine, if_exists="append", index=False)
print("Tabla de hechos cargada")