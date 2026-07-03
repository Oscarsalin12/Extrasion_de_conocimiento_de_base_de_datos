create database modelstartTobi
go
use modelstartTobi

create table DimPaciente(
dimPacienteSK int primary key identity,
id_paciente varchar(10) not null,
paciente varchar(50) not null
);

create table DimEspecialidad(
dimEspecialidadSK int primary key identity,
id_especialidad varchar(10) not null,
especialidad varchar(30) not null
);

create table DimMedico(
dimMedicoSK int primary key identity,
medico varchar(50) not null
);

create table DimCiudad(
dimCiudadSK int primary key identity,
ciudad varchar(40) not null
);

create table DimTConsulta(
dimTConsultaSK int primary key identity,
tipo_consulta varchar(40) not null
);

create table DimTiempo(
dimTiempoSK int primary key identity,
fecha datetime not null,
dia int not null,
mes int not null,
anio int not null
);

create table FactConsultas(
consultasSK int primary key identity,
dimPacienteSK int not null,
dimMedicoSK int not null,
dimEspecialidadSK int not null,
dimCiudadSK int not null,
dimTConsultaSK int not null,
dimTiempoSK int not null,
costo int not null,
cantidadConsultas int not null,
  CONSTRAINT FK_paciente FOREIGN KEY (dimPacienteSK) REFERENCES DimPaciente(dimPacienteSK),
  CONSTRAINT FK_medico FOREIGN KEY (dimMedicoSK) REFERENCES DimMedico(dimMedicoSK),
  CONSTRAINT FK_especialidad FOREIGN KEY (dimEspecialidadSK) REFERENCES DimEspecialidad(dimEspecialidadSK),
  CONSTRAINT FK_ciudad FOREIGN KEY (dimCiudadSK) REFERENCES DimCiudad(dimCiudadSK),
  CONSTRAINT FK_tconsulta FOREIGN KEY (dimTConsultaSK) REFERENCES DimTConsulta(dimTConsultaSK),
  CONSTRAINT FK_tiempo FOREIGN KEY (dimTiempoSK) REFERENCES DimTiempo(dimTiempoSK),
);