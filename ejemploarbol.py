import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# 1. Generación del DataFrame
datos = {
    'Antiguedad_Meses': [5, 12, 24, 36, 2, 48, 60, 8, 15, 20, 1, 40, 50, 10, 30],
    'Gasto_Promedio_MXN': [1500, 2500, 5000, 8000, 800, 12000, 15000, 1800, 3000, 4500, 500, 9000, 11000, 2000, 6000],
    'Visitas_Mensuales': [1, 2, 4, 6, 1, 8, 10, 2, 3, 4, 1, 7, 9, 2, 5],
    'Tipo_Membresia': ['Básica', 'Básica', 'Plata', 'Oro', 'Básica', 'Oro', 'Oro', 'Básica', 'Plata', 'Plata', 'Básica', 'Oro', 'Oro', 'Básica', 'Plata']
}

df = pd.DataFrame(datos)

X = df[['Antiguedad_Meses', 'Gasto_Promedio_MXN', 'Visitas_Mensuales']] 
y = df['Tipo_Membresia']  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

print("--- División de Datos para la IA ---")
print(f"Registros de entrenamiento: {len(X_train)}")
print(f"Registros de prueba: {len(X_test)}\n")

arbol_clasificacion = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=42)
arbol_clasificacion.fit(X_train, y_train)
predicciones = arbol_clasificacion.predict(X_test)
precision = accuracy_score(y_test, predicciones)

print("--- RENDIMIENTO DEL MODELO ---")
print(f"Precisión Global (Accuracy): {precision * 100:.2f}%")
print("\nReporte Estadístico Detallado:")
print(classification_report(y_test, predicciones))

plt.figure(figsize=(14, 8))
plot_tree(arbol_clasificacion, 
          feature_names=X.columns, 
          class_names=arbol_clasificacion.classes_, 
          filled=True, 
          rounded=True, 
          fontsize=10)

plt.title("Árbol de Decisión Entrenado (Asignación de Membresía)", fontsize=14)
plt.savefig('mi_arbol_ia.png', dpi=300, bbox_inches='tight')
print("¡Gráfico guardado con éxito como 'mi_arbol_ia.png'!")
plt.close() 