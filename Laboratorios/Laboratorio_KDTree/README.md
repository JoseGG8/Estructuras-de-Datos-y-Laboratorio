# Laboratorio: Estructuras de Datos Espaciales - K-D Tree

## 🎯 Objetivos

* **Implementar** una estructura de datos K-D Tree eficiente para la organización de puntos en un espacio bidimensional.
* **Desarrollar** algoritmos de búsqueda espacial, específicamente Búsqueda por Radio y Vecino más Cercano (KNN).
* **Comparar** el rendimiento computacional entre la estructura de árbol y el algoritmo de Fuerza Bruta bajo diferentes métricas de volumen de datos.
* **Visualizar** mediante herramientas gráficas cómo el árbol divide el espacio y optimiza el proceso de filtrado de puntos.
* **Analizar** el impacto de parámetros como la cardinalidad de los datos y el radio de búsqueda en la eficiencia de la poda (pruning).

Este proyecto implementa y analiza el rendimiento de un **Árbol K-Dimensional (K-D Tree)** en 2 dimensiones, comparando su eficiencia contra algoritmos de **Fuerza Bruta** en tareas de búsqueda espacial.

## 📂 Estructura del Proyecto

El laboratorio se divide en los siguientes componentes:

* **`KD_Tree.py`**: El núcleo del proyecto. Contiene la definición de la clase `Nodo` y la clase `KD_Tree`. Está optimizado para 2 dimensiones y permite la construcción del árbol y la ejecución de métodos de búsqueda.
* **`funciones_graficas.py`**: Módulo auxiliar que contiene funciones basadas en `matplotlib`. Su objetivo es desacoplar la lógica de visualización del procesamiento de datos para mantener un código limpio.
* **`test.ipynb`**: Notebook destinado a la validación visual. Aquí se invocan las funciones de graficación para observar el comportamiento de la **Búsqueda por Vecino más Cercano (KNN)** y la **Búsqueda por Radio**.
* **`analisis.ipynb`**: Notebook de experimentación técnica. Contiene la implementación de Fuerza Bruta y las celdas de comparación de tiempos (benchmarking) entre ambas estrategias, incluyendo las conclusiones derivadas de los resultados.

---

## 🚀 Guía de Uso

### Visualización de Algoritmos
Para ver el árbol en acción y cómo delimita el espacio:
1. Abre `test.ipynb`.
2. Ejecuta las celdas en orden cronológico.
3. Se generarán gráficos interactivos/estáticos de las búsquedas realizadas.

### Análisis de Rendimiento (Benchmark)
Para comparar la eficiencia del K-D Tree frente a la Fuerza Bruta:
1. Abre `analisis.ipynb`.
2. Ejecuta todas las celdas para observar las métricas basadas en el **promedio de tiempos de ejecución**.
3. **Personalización:** Si deseas probar diferentes escenarios, modifica la cantidad de datos en la primera celda o ajusta los parámetros de los métodos de búsqueda (como el radio).

---

## 🛠️ Detalles de Implementación

> [!IMPORTANT]
> El K-D Tree almacena nodos con coordenadas bidimensionales. Para las comparaciones de tiempo, se utiliza un promedio de múltiples ejecuciones para mitigar variaciones térmicas o de procesamiento del sistema.

### Componentes principales:
* **Construcción:** El árbol se genera a partir de un conjunto de puntos dado.
* **Búsqueda por Radio:** Implementa poda (pruning) para evitar recorrer ramas que no intersectan el área de búsqueda.
* **Fuerza Bruta:** Implementada en listas para servir como línea base (baseline) de comparación.

---

## 📝 Notas
* Asegúrate de tener instaladas las dependencias de `matplotlib` y `numpy` (si aplica).
* El archivo `KD_Tree.py` debe estar en el mismo directorio que los notebooks para que las importaciones funcionen correctamente.
