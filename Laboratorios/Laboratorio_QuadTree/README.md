# 🌳 Laboratorio: QuadTree — Búsqueda Espacial Eficiente

> **Curso:** Estructuras de Datos y Laboratorio  
> **Lenguaje:** Python 3.12  
> **Temas:** QuadTree, Nearest Neighbor Search (NNS), Búsqueda por Radio, Análisis de Complejidad

---

## 📋 Tabla de Contenidos

1. [¿Qué es un QuadTree?](#-qué-es-un-quadtree)
2. [Descripción del Laboratorio](#-descripción-del-laboratorio)
3. [Estructura del Proyecto](#-estructura-del-proyecto)
4. [Tecnologías Utilizadas](#-tecnologías-utilizadas)
5. [Instalación y Requisitos](#-instalación-y-requisitos)
6. [Uso — Guía Paso a Paso](#-uso--guía-paso-a-paso)
7. [API de la Clase QuadTree](#-api-de-la-clase-quadtree)
8. [Funciones Gráficas](#-funciones-gráficas)
9. [Análisis de Rendimiento](#-análisis-de-rendimiento)
10. [Conclusiones](#-conclusiones)

---

## 🌐 ¿Qué es un QuadTree?

Un **QuadTree** es una estructura de datos jerárquica en forma de árbol en la que cada nodo interno tiene exactamente **cuatro hijos**, uno por cada cuadrante del plano 2D (NE, NO, SE, SO). Se utiliza para **particionar recursivamente un espacio bidimensional** con el objetivo de organizar datos espaciales (coordenadas) de forma eficiente.

### Principio de funcionamiento

La idea central es sencilla: dado un conjunto de puntos en un plano, el QuadTree divide el espacio en cuatro cuadrantes mediante un punto medio calculado a partir de los extremos del conjunto actual. Este proceso se repite recursivamente en cada cuadrante hasta que cada región contenga un único punto, que se convierte en un **nodo hoja**.

```
         Espacio original
        ┌────────┬────────┐
        │   NO   │   NE   │
        │  [p1]  │ [p2,p3]│
        ├────────┼────────┤
        │   SO   │   SE   │
        │  [p4]  │  [p5]  │
        └────────┴────────┘
               ⬇
     Cada cuadrante se subdivide
     hasta tener 1 punto por región
```

### ¿Para qué sirve?

El QuadTree reduce drásticamente el número de comparaciones necesarias para operaciones como:
- **Vecino más cercano (NNS):** en lugar de comparar contra todos los N puntos, el árbol guía la búsqueda hacia las regiones más prometedoras y descarta ("poda") las ramas que no pueden contener la respuesta.
- **Búsqueda por radio:** en lugar de verificar todos los puntos, solo se exploran las ramas cuyas cajas delimitadoras intersectan con el círculo de búsqueda.

### Generalización N-dimensional

La implementación de este laboratorio generaliza el concepto a **N dimensiones**: en 2D hay 4 hijos (2²), en 3D hay 8 hijos (2³ — lo que se conoce como *Octree*), y así sucesivamente. La asignación de cada punto a su cuadrante se realiza mediante **operaciones de bits**, lo que hace el código elegante y eficiente.

### Complejidad

| Operación | Caso promedio | Caso peor |
|---|---|---|
| Construcción | O(n log n) | O(n²) |
| Vecino más cercano | O(log n) | O(n) |
| Búsqueda por radio (radio pequeño) | O(log n + k) | O(n) |
| Búsqueda por radio (radio grande) | O(n) | O(n) |

> *k* = número de puntos encontrados dentro del radio.

---

## 📌 Descripción del Laboratorio

Este laboratorio implementa un **QuadTree desde cero en Python** y lo utiliza para resolver dos problemas clásicos de búsqueda espacial:

1. **Nearest Neighbor Search (NNS):** dado un punto de consulta Q, encontrar el punto más cercano en el conjunto de datos.
2. **Búsqueda por Radio:** dado un punto Q y un radio R, encontrar todos los puntos que se encuentran dentro de la circunferencia de centro Q y radio R, y retornar también los 20 más cercanos.

Ambos algoritmos son comparados contra sus equivalentes de **fuerza bruta** (iteración sobre una lista) para evidenciar la superioridad del QuadTree con grandes volúmenes de datos.

---

## 📁 Estructura del Proyecto

```
Laboratorio_QuadTree/
│
├── QuadTree.py               # Implementación completa del QuadTree
├── funciones_graficas.py     # Visualizaciones con Matplotlib
├── test.ipynb                # Notebook de demostración visual
├── analisis.ipynb            # Notebook de análisis de rendimiento
└── README.md                 # Este archivo
```

### Descripción de archivos

**`QuadTree.py`**  
Contiene las tres clases del núcleo de la solución:
- `Nodo_Hoja` — representa un punto final del árbol (coordenada sin hijos).
- `Nodo_intermedio` — nodo interno que almacena la caja delimitadora (AABB), el centro del cuadrante y referencias a sus hijos.
- `QuadTree` — clase principal con los métodos de construcción y búsqueda.

**`funciones_graficas.py`**  
Módulo de visualización que genera gráficas interactivas con Matplotlib para visualizar los resultados de las búsquedas y comparar el rendimiento entre algoritmos.

**`test.ipynb`**  
Notebook pensado para demostrar visualmente el funcionamiento del árbol. Contiene ejemplos de uso de `graficar_busqueda_radio()` y `graficar_vecino_cercano()` con 10.000 puntos generados aleatoriamente.

**`analisis.ipynb`**  
Notebook de benchmarking. Implementa los algoritmos de fuerza bruta equivalentes y mide tiempos de ejecución promediados en 100 iteraciones para distintos tamaños de datos (desde 100 hasta 500.000 puntos).

---

## 🛠 Tecnologías Utilizadas

| Tecnología | Versión | Rol en el proyecto |
|---|---|---|
| **Python** | 3.12 | Lenguaje principal |
| **Matplotlib** | 3.x | Visualización de puntos, radios y gráficas de rendimiento |
| **NumPy** | 1.x | Importado como dependencia de Matplotlib |
| **math** (stdlib) | — | Cálculo de distancias euclidianas |
| **random** (stdlib) | — | Generación de datos de prueba aleatorios |
| **time** (stdlib) | — | Medición de tiempos de ejecución con `perf_counter` |
| **Jupyter Notebook** | — | Entorno interactivo para pruebas y análisis |

---

## ⚙️ Instalación y Requisitos

### Prerrequisitos

- Python 3.12 o superior
- `pip` instalado

### Instalación de dependencias

```bash
pip install matplotlib numpy jupyter
```

### Ejecución

**Para abrir los notebooks:**

```bash
jupyter notebook
```

Luego navegar a `test.ipynb` para la demostración visual o `analisis.ipynb` para el análisis de rendimiento.

**Para usar la clase directamente en un script:**

```python
from QuadTree import QuadTree

datos = [(1, 2), (3, 4), (5, 1), (2, 8)]
arbol = QuadTree(datos, dimensiones=2)
arbol.construir_arbol()
```

---

## 🚀 Uso — Guía Paso a Paso

### 1. Crear los datos

Los datos deben ser una lista de tuplas con coordenadas numéricas.

```python
import random

# Generar 10.000 puntos aleatorios en un espacio de 1000x1000
datos = [(random.randint(0, 1000), random.randint(0, 1000)) for _ in range(10000)]
```

### 2. Instanciar y construir el árbol

```python
from QuadTree import QuadTree

arbol = QuadTree(datos, dimensiones=2)
arbol.construir_arbol()
```

> ⚠️ `construir_arbol()` debe llamarse explícitamente después de crear la instancia. El constructor solo inicializa los atributos.

### 3. Búsqueda del vecino más cercano

```python
punto_consulta = (500, 500)
vecino, distancia = arbol.buscar_vecino_cercano(punto_consulta)

print(f"Vecino más cercano: {vecino}")
print(f"Distancia: {distancia:.4f}")
```

**Retorna:** una tupla `(coordenada, distancia)` donde `coordenada` es una tupla `(x, y)` y `distancia` es un `float`.

### 4. Búsqueda por radio

```python
punto_consulta = (400, 400)
radio = 200

todos_los_puntos, top_20 = arbol.buscar_por_radio(punto_consulta, radio)

print(f"Puntos dentro del radio: {len(todos_los_puntos)}")
print(f"Los 20 más cercanos: {top_20}")
```

**Retorna:** una tupla `(lista_todos, lista_top_20)`:
- `lista_todos` — todos los puntos dentro del radio, ordenados por distancia ascendente.
- `lista_top_20` — los primeros 20 elementos de `lista_todos`.

### 5. Visualizar los resultados

```python
from funciones_graficas import graficar_busqueda_radio, graficar_vecino_cercano

# Visualizar búsqueda por radio
graficar_busqueda_radio(arbol, (400, 400), 200)

# Visualizar vecino más cercano
graficar_vecino_cercano(arbol, (500, 500))
```

### 6. Uso en 3D (generalización)

La implementación soporta dimensiones arbitrarias. Para datos 3D:

```python
datos_3d = [(random.random(), random.random(), random.random()) for _ in range(5000)]
arbol_3d = QuadTree(datos_3d, dimensiones=3)  # Octree: 8 hijos por nodo
arbol_3d.construir_arbol()

vecino, dist = arbol_3d.buscar_vecino_cercano((0.5, 0.5, 0.5))
```

---

## 📐 API de la Clase QuadTree

### `QuadTree(datos, dimensiones)`

**Constructor.**

| Parámetro | Tipo | Descripción |
|---|---|---|
| `datos` | `list[tuple]` | Lista de tuplas de coordenadas numéricas |
| `dimensiones` | `int` | Número de dimensiones del espacio (2 para 2D, 3 para 3D, etc.) |

---

### `construir_arbol(nodo=None)`

Construye el árbol recursivamente a partir de `self.datos`. Debe llamarse antes de cualquier búsqueda. No recibe parámetros en su uso normal (el parámetro `nodo` es de uso interno recursivo).

---

### `buscar_vecino_cercano(punto_Q) → (tuple, float)`

Encuentra el punto más cercano a `punto_Q` usando el algoritmo NNS con poda de ramas.

| Parámetro | Tipo | Descripción |
|---|---|---|
| `punto_Q` | `tuple` | Punto de consulta, ej. `(500, 500)` |

**Retorna:** `(coordenada_vecino, distancia)` — la coordenada del vecino más cercano y su distancia euclidiana.

---

### `buscar_por_radio(punto_Q, radio) → (list, list)`

Encuentra todos los puntos dentro de un radio circular alrededor de `punto_Q`.

| Parámetro | Tipo | Descripción |
|---|---|---|
| `punto_Q` | `tuple` | Centro de la búsqueda |
| `radio` | `float` | Radio de la circunferencia de búsqueda |

**Retorna:** `(todos_los_puntos, top_20)` — lista completa ordenada por distancia y los 20 más cercanos.

---

### `calcular_distancia(p1, p2) → float`

Método auxiliar público. Calcula la distancia euclidiana entre dos puntos de N dimensiones.

---

## 📊 Funciones Gráficas

El módulo `funciones_graficas.py` expone cuatro funciones de visualización:

### `graficar_busqueda_radio(arbol, punto_objetivo, radio)`

Genera un scatter plot que muestra todos los puntos del árbol en gris tenue, los puntos dentro del radio en **rojo**, el punto objetivo como una **X azul**, los 20 más cercanos en **amarillo** y la circunferencia del radio como un círculo punteado azul.

### `graficar_vecino_cercano(arbol, punto_objetivo)`

Genera una gráfica centrada en el punto objetivo y su vecino más cercano. Muestra el objetivo como una **X azul**, el vecino como un **círculo rojo** y una línea punteada que los une indicando la distancia. El resto de los puntos se muestran como contexto tenue.

### `graficar_comparativa(resultados)`

Recibe el diccionario de resultados de la función `medir_rendimiento()` y genera dos gráficas lado a lado comparando los tiempos de ejecución de QuadTree vs. Fuerza Bruta para NNS y búsqueda por radio en función del número de puntos N.

### `graficar_rendimiento_por_radio(arbol, punto_Q, radios_lista)`

Mide y grafica cómo varía el tiempo de ejecución de `buscar_por_radio()` al aumentar el radio de búsqueda, evidenciando la relación entre el tamaño del radio y el número de ramas que el árbol debe explorar.

---

## 📈 Análisis de Rendimiento

### Vecino más cercano: QuadTree vs. Fuerza Bruta

Los experimentos en `analisis.ipynb` prueban ambos algoritmos con tamaños de datos desde 100 hasta 500.000 puntos, midiendo el **tiempo promedio de 100 ejecuciones** para suavizar variaciones del sistema.

Los resultados muestran un patrón claro:

- **Con pocos datos (< 500 puntos):** la fuerza bruta puede igualar o superar al QuadTree. Esto ocurre porque las CPUs modernas están altamente optimizadas para iterar listas contiguas en memoria, mientras que el QuadTree incurre en un costo fijo de lógica de decisión y acceso a punteros dispersos.

- **Con datos moderados (1.000 – 10.000 puntos):** el QuadTree empieza a mostrar ventaja.

- **A partir de 10.000 puntos:** el tiempo de la fuerza bruta crece de forma lineal (O(n)), mientras que el QuadTree se mantiene prácticamente constante (O(log n)), separándose por **órdenes de magnitud**.

### Búsqueda por radio: efecto del tamaño del radio

A diferencia de la fuerza bruta —cuyo tiempo es completamente independiente del radio— el QuadTree tiene una relación directa entre el radio y el tiempo de ejecución:

- **Radio pequeño:** el árbol descarta rápidamente la mayoría de las ramas mediante la verificación AABB (Axis-Aligned Bounding Box), resultando en tiempos muy bajos.
- **Radio grande (que abarca casi toda la región):** el árbol se ve obligado a explorar prácticamente todas las ramas, aproximándose al comportamiento de fuerza bruta.

Las gráficas en `analisis.ipynb` evidencian que esta relación tiene un **comportamiento aproximadamente lineal** respecto al radio: a mayor radio, más ramas intersectan con el círculo de búsqueda y más tiempo toma la operación.

---

## 🧠 Conclusiones

**1. Los QuadTrees son una solución eficiente y elegante para búsquedas espaciales.**  
La subdivisión recursiva del espacio permite descartar grandes regiones sin examinar cada punto individualmente, logrando una complejidad promedio O(log n) frente al O(n) de la fuerza bruta.

**2. La generalización N-dimensional mediante operaciones de bits es un acierto de diseño.**  
Al usar `indice_hijo |= (1 << i)` para asignar cada punto a su cuadrante según si supera el centro en cada dimensión, la implementación escala naturalmente de 2D a 3D o más sin cambiar la lógica central.

**3. La poda (pruning) es la clave del rendimiento.**  
El algoritmo NNS no solo baja por la rama más prometedora, sino que después verifica cada rama hermana usando la distancia mínima a la caja delimitadora. Si esa distancia mínima ya supera al mejor candidato encontrado, la rama se descarta completamente. Esta poda es lo que evita explorar zonas del espacio que no pueden mejorar el resultado.

**4. El QuadTree no siempre gana — el contexto importa.**  
Para conjuntos de datos pequeños (< 500 puntos), la fuerza bruta puede ser más rápida debido a la localidad de referencia en memoria y al overhead de la lógica recursiva del árbol. La decisión de usar un QuadTree debe considerar el volumen de datos y la frecuencia de consultas.

**5. El radio es un factor determinante en la búsqueda espacial.**  
Un radio que abarca casi todo el espacio anula la ventaja del árbol. El QuadTree es especialmente poderoso cuando se trabaja con radios acotados en conjuntos de datos grandes y dispersos.

**6. La construcción del árbol es un costo único amortizable.**  
El árbol se construye una sola vez y puede responder múltiples consultas en O(log n). En aplicaciones reales (mapas, sistemas de detección de colisiones, bases de datos geoespaciales) este costo de preprocesamiento se amortiza rápidamente con el volumen de consultas.

---

## 📚 Referencias

- Samet, H. (1984). *The Quadtree and Related Hierarchical Data Structures*. ACM Computing Surveys.
- de Berg, M. et al. (2008). *Computational Geometry: Algorithms and Applications*, 3rd ed. Springer.
- Documentación oficial de [Matplotlib](https://matplotlib.org/stable/index.html)
- Documentación oficial de [Python 3.12](https://docs.python.org/3.12/)
