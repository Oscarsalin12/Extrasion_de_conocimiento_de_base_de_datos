import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mssql+pyodbc://sa:Admsis123@localhost/startmodelg2?driver=ODBC+Driver+17+for+SQL+Server")

print(pd.read_sql("SELECT DB_NAME() as bd",engine))
ventas = pd.read_csv("ventascursos_limpias.csv")
ventas['fecha']=pd.to_datetime(ventas["fecha"]).dt.date
ventas['cantidadVentas']=1

#dimension curso
dimcurso=ventas[['id_curso','curso']]
dimcurso=dimcurso.drop_duplicates()
dimcurso.to_sql("dimCurso",engine,if_exists="append",index=False)
print("Dimensión Curso cargada")
#dimension cliente
dimcliente=ventas[['id_cliente', 'nombre_cliente']]
dimcliente=dimcliente.drop_duplicates()
dimcliente.to_sql("dimCliente",engine,if_exists="append",index=False)
print ("dimension clientes cargados")
#dim instructor
diminstructor=ventas[['instructor']]
diminstructor=diminstructor.drop_duplicates()
diminstructor.to_sql("dimInstructor",engine,if_exists="append",index=False)
print("Dimensión Instructor cargada")
#dim modalidad
dimmodalidad=ventas[['modalidad']]
dimmodalidad=dimmodalidad.drop_duplicates()
dimmodalidad.to_sql("dimModalidad",engine,if_exists="append",index=False
)
print("Dimensión Modalidad cargada")
#dim ciudad
dimciudad = ventas[['ciudad']]
dimciudad = dimciudad.drop_duplicates()
dimciudad.to_sql("dimCiudad", engine, if_exists="append", index=False)
print("Dimensión Ciudad cargada")
#dim tiempo
dimtiempo = pd.DataFrame()
dimtiempo["fecha"] = pd.to_datetime(ventas["fecha"])
dimtiempo["dia"] = dimtiempo["fecha"].dt.day
dimtiempo["mes"] = dimtiempo["fecha"].dt.month
dimtiempo["anio"] = dimtiempo["fecha"].dt.year

dimtiempo = dimtiempo.drop_duplicates()

dimtiempo.to_sql("dimTiempo", engine, if_exists="append", index=False)

print("Dimensión Tiempo cargada")
#cursos
factventas=ventas.copy()
factventas = factventas = ventas.merge(dimcurso[['id_curso']], on="id_curso", how="left")
#clientes
factventas = factventas.merge(dimcliente[['id_cliente']], on="id_cliente", how="left")
#instructores
factventas = factventas.merge(diminstructor[['instructor']], on="instructor", how="left")
#modalidades
factventas = factventas.merge(dimmodalidad[['modalidad']], on="modalidad", how="left")
#ciudades
factventas = factventas.merge(dimciudad[['ciudad']], on="ciudad", how="left")
#tiempo
factventas = factventas.merge(dimtiempo[['fecha']], on="fecha", how="left")