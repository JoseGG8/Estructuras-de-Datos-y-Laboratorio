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
7. [Clase QuadTree](#-api-de-la-clase-quadtree)
8. [Funciones Gráficas](#-funciones-gráficas)
9. [Análisis de Rendimiento](#-análisis-de-rendimiento)
10. [Conclusiones](#-conclusiones)

---

## 🌐 ¿Qué es un QuadTree?

Un **QuadTree** es una estructura de datos jerárquica en forma de árbol en la que cada nodo interno tiene exactamente **2^dimensiones** hijos. Se utiliza para **particionar recursivamente un espacio n-dimensional** con el objetivo de organizar datos espaciales (coordenadas) de forma eficiente.




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
├── funciones_graficas.py     # funciones para visualizaciones con Matplotlib
├── test.ipynb                # Notebook de demostración visual
├── analisis.ipynb            # Notebook de análisis de rendimiento (usa funciones_graficas.py)
└── README.md                 # Este archivo
```

### Descripción de archivos

**`QuadTree.py`**  
Contiene las tres clases del núcleo de la solución:
- `Nodo_Hoja` — representa un punto final del árbol (coordenada sin hijos).
- `Nodo_intermedio` — nodo interno que almacena la caja delimitadora , el centro del cuadrante y referencias a sus hijos.
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
| **Python** |
| **Matplotlib** | 
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

## 🚀 Uso — Ejecución sin escribir código
 
Los notebooks están diseñados para ejecutarse celda por celda desde Jupyter. No es necesario escribir ninguna línea de código.
 
### Cómo abrir el entorno
 
1. Abrir una terminal en la carpeta `Laboratorio_QuadTree/`
2. Ejecutar:
   ```bash
   jupyter notebook
   ```
3. El navegador abrirá automáticamente el explorador de Jupyter. Desde ahí seleccionar el notebook deseado.
---
 
### `test.ipynb` — Demostración visual
 
Este notebook muestra las búsquedas de forma gráfica sobre 10.000 puntos aleatorios. Ejecutar las celdas **en orden de arriba hacia abajo**:
 
| # | Qué hace la celda |
|---|---|
| 1 | Importa librerías y genera los 10.000 puntos aleatorios |
| 2 | Construye el árbol sobre esos datos |
| 3 | Genera la gráfica de **búsqueda por radio** (radio = 200, centro en (400, 400)) — muestra los puntos dentro del radio en rojo y los 20 más cercanos en amarillo |
| 4 | Genera la gráfica de **vecino más cercano** (desde el punto (500, 500)) — resalta el vecino encontrado con un círculo rojo y la distancia |
 
> ℹ️ Como los datos se generan aleatoriamente, cada ejecución produce un conjunto diferente de puntos. Los resultados varían entre corridas, pero el comportamiento del árbol es siempre el mismo.
 
---
 
### `analisis.ipynb` — Análisis de rendimiento
 
Este notebook compara los tiempos del QuadTree contra la fuerza bruta. Ejecutar las celdas **en orden de arriba hacia abajo**:
 
| # | Qué hace la celda |
|---|---|
| 1 | Importa librerías, genera datos y construye el árbol. Define también las funciones de fuerza bruta |
| 2 | Mide y muestra el **tiempo promedio (100 ejecuciones)** de vecino más cercano: QuadTree vs. fuerza bruta |
| 3 | Mide y muestra el **tiempo promedio (100 ejecuciones)** de búsqueda por radio: QuadTree vs. fuerza bruta |
| 4 | Genera la gráfica de **tiempo vs. radio** para el QuadTree, mostrando cómo crece el tiempo al aumentar el radio de búsqueda |
| 5 | Define la función `medir_rendimiento()` que prueba ambos algoritmos con distintos tamaños de datos |
| 6 | Ejecuta las pruebas con tamaños desde 100 hasta 500.000 puntos y genera las **gráficas comparativas finales** ⚠️ esta celda puede tardar varios minutos |
 
> ⚠️ La última celda de `analisis.ipynb` prueba hasta 500.000 puntos y puede tardar entre 3 y 8 minutos dependiendo del equipo. Es normal que parezca que no responde durante ese tiempo — el kernel está trabajando.
 
---
 
## 📐La Clase QuadTree
 
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
 
**2. La generalización N-dimensional mediante operaciones de bits.**  
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
 
