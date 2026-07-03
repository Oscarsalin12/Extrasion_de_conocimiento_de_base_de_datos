import pandas as pd 
from sqlalchemy import create_engine
#crear conexion con base de datos 
engine = create_engine("mssql+pyodbc://sa:Admsis123@localhost:1433/modelstartTobi?driver=ODBC+Driver+17+for+SQL+Server")
print (pd.read_sql("SELECT DB_NAME() as bd",engine))

consultas = pd.read_csv("consultasmedicaslimpio.csv")
consultas['fecha']=pd.to_datetime(consultas["fecha"]).dt.date

consultas["cantidadConsultas"]=1
#pacientes no.1
dimpaciente = consultas[["id_paciente", "paciente"]]
dimpaciente = dimpaciente.drop_duplicates()
dimpaciente.to_sql("DimPaciente", engine, if_exists="append", index=False)
print("Dimensión Paciente cargada")

#especialidades no.2
dimespecialidad = consultas[["id_especialidad", "especialidad"]]
dimespecialidad = dimespecialidad.drop_duplicates()
dimespecialidad.to_sql("DimEspecialidad", engine, if_exists="append", index=False)
print("Dimensión Especialidad cargada")

#medicos no.3
dimmedico = consultas[["medico"]]
dimmedico = dimmedico.drop_duplicates()
dimmedico.to_sql("DimMedico", engine, if_exists="append", index=False)

print("Dimensión Medico cargada")

#cuidades no.4
dimciudad = consultas[["ciudad"]]
dimciudad = dimciudad.drop_duplicates()
dimciudad.to_sql("DimCiudad", engine, if_exists="append", index=False)
print("Dimensión Ciudad cargada")

#tipo de consulta no.5
dimtipoconsulta = consultas[["tipo_consulta"]]
dimtipoconsulta = dimtipoconsulta.drop_duplicates()
dimtipoconsulta.to_sql("DimTConsulta", engine, if_exists="append", index=False)
print("Dimensión Tipo Consulta cargada")

#tiempo no.6
dimtiempo = pd.DataFrame()
dimtiempo["fecha"]= consultas[["fecha"]]
dimtiempo["dia"] =pd.to_datetime(dimtiempo["fecha"]).dt.day
dimtiempo["mes"] = pd.to_datetime(dimtiempo["fecha"]).dt.month
dimtiempo["anio"] = pd.to_datetime(dimtiempo["fecha"]).dt.year
dimtiempo = dimtiempo.drop_duplicates()
dimtiempo.to_sql("DimTiempo", engine, if_exists="append", index=False)
print("Dimensión Tiempo cargada")

#consultas de sql 
dimpaciente_sql = pd.read_sql("SELECT * FROM DimPaciente", engine)
dimespecialidad_sql = pd.read_sql("SELECT * FROM DimEspecialidad", engine)
dimmedico_sql = pd.read_sql("SELECT * FROM DimMedico", engine)
dimciudad_sql = pd.read_sql("SELECT * FROM DimCiudad", engine)
dimtipoconsulta_sql = pd.read_sql("SELECT * FROM DimTConsulta", engine)
dimtiempo_sql = pd.read_sql("SELECT * FROM DimTiempo", engine)
dimtiempo_sql["fecha"]= pd.to_datetime(dimtiempo_sql["fecha"]).dt.date

factconsultas = consultas.copy()

factconsultas = factconsultas.merge(dimpaciente_sql[['dimPacienteSK','id_paciente']], on="id_paciente", how="left")
factconsultas = factconsultas.merge(dimespecialidad_sql[['dimEspecialidadSK','id_especialidad']], on="id_especialidad", how="left")
factconsultas = factconsultas.merge(dimmedico_sql[['dimMedicoSK','medico']], on="medico", how="left")
factconsultas = factconsultas.merge(dimciudad_sql[['dimCiudadSK','ciudad']], on="ciudad", how="left")
factconsultas = factconsultas.merge(dimtipoconsulta_sql[['dimTConsultaSK','tipo_consulta']], on="tipo_consulta", how="left")
factconsultas = factconsultas.merge(dimtiempo_sql[['dimTiempoSK','fecha']], on="fecha", how="left")

factconsultas = factconsultas[["dimPacienteSK", "dimEspecialidadSK", "dimMedicoSK","dimCiudadSK","dimTConsultaSK","dimTiempoSK","costo","cantidadConsultas"]]
factconsultas.to_sql("FactConsultas", engine, if_exists="append", index=False)
print("Tabla de hechos cargada")