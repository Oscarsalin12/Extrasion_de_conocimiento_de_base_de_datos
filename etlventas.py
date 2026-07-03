import pandas as pd 

ventas = pd.read_csv('ventas.csv')
print(ventas.head())
print(ventas.info())
print(ventas.describe())

# identificar problemas 
print(ventas.isnull().sum())

# identifacr diplicados
print(ventas.duplicated().sum())

# eliminar duplicados
ventas = ventas.drop_duplicates()
print(ventas.duplicated().sum())

# eliminar filas con valores nulos
#ventas = ventas.dropna()
#print(ventas.isnull().sum())
ventas["Ciudad"] = ventas['Ciudad'].fillna("Desconocida")
print(ventas.isnull().sum())

#transformar datos 
ventas ["TotalVenta"] = ventas["Cantidad"] * ventas["PrecioUnitario"]
ventas["Mes"] = pd.to_datetime(ventas["Fecha"]).dt.month
ventas["Anio"] = pd.to_datetime(ventas["Fecha"]).dt.year

print(ventas.head())

# estandarizar texto
ventas["Producto"] = (ventas["Producto"].str.strip().str.title())
print(ventas.head())

print(ventas.groupby("Ciudad")["TotalVenta"].sum())
print(ventas.groupby("Producto")["TotalVenta"].sum())
print(ventas.groupby("Producto")["Cantidad"].sum().sort_values(ascending=False).head(5))

ventas.to_csv("ventas_limpias.csv", index=False)


