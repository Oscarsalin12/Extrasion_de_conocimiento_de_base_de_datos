library(readr)
library(dplyr)

datos <- read.csv("C:/Users/salin/Documents/Extrasion_de_conocimiento_de_base_de_datos/pacientesdiabetes.csv")

head(datos) #primeros
tail(datos) #ultimos
names(datos) #nombre de columnas
dim(datos) #filas y columnas
nrow(datos) # numero ty filas 
ncol(datos) # nemeros columnas

View(datos)

datos$Edad #muestra 1 columna
datos[,c("Edad","Sexo","Glucosa")]#muesta varias columnas
datos[3,] # muestra n fila
datos[1:10] #muestra 

str(datos) #muestra la estructura del data frame
summary(datos) #muestra estadisticos del df
mean(datos$IMC) #media de imc
mean(datos$Edad)
mean(datos$Estatura)
mean(datos$Glucosa)

min(datos$Edad) #minimo de una columna
max(datos$Estatura) #maximo de una columna
sd(datos$Edad)# desviacion estandar de una columna

sum(!is.na(datos$Glucosa))#cuenta no nulos
sum(is.na(datos$Glucosa)) # cuenta nulos

colSums(is.na(datos))# identifiaca valores nulos
sum(duplicated(datos)) #  detecta registros duplicados

datoslimpios <- na.omit(datos) #quita filas con datos faltantes
datoslimpios

summarise(
  group_by(datoslimpios,Sexo),
  PromedioGlucosa = mean(Glucosa)
  ) #manejo de agrupaciones en data frame
mayores <- filter(datoslimpios,Edad>60)
mayores

mujeresdiabetes <- filter(datoslimpios,Sexo =="Femenino",Diagnostico =="Diabetes")
mujeresdiabetes

Hombresdiabetes <- filter(datoslimpios,Sexo =="Masculino",Diagnostico =="Diabetes")
Hombresdiabetes

hist(datos$Edad)
barplot(table(datoslimpios$Diagnostico))

frecuencia <- table(datoslimpios$Diagnostico)
pie(frecuencia,main = "Datos por Diagnostico")