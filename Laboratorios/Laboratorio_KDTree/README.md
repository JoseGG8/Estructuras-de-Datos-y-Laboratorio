Este laboratorio tiene la siguiente estructura: 
análisis.ipynb
funciones_graficas.py
KD_Tree.py
test.ipynb

Explicación componentes:
KD_Tree.py es el archivo donde se construyó el arbol KD, sus métodos y la clase nodo
el arbol kd fue construido para 2 dimensiones y sus metodos responden a esto, este arbol almacena nodos con las coordenadas de los datos que se le pasen. Como utilizar? esta clase se importa en los otros archivos para implementar instancias de arboles kd y desarrollar el laboratorio.

funciones_graficas.py contiene las funciones para crear las graficas con matplotlib, este archivo se creó con el ánimo de mantener una estructura más limpia en el proyecto. Como utilizar? estas funciones se implementan en test.py para visualización directa de las gráficas de busqueda de vecino más cercano y búsqueda por radio.
estas funciones implementan los metodos de KD_Tree.py para buscar.

test.ipynb contiene las gráficas que se crean con las funciones de funciones_graficas.py. Para utilizar este archivo debes ejecutar todas las celdas en orden y se podrán visualizar las gráficas.

analisis.ipynb es un notebook que contiene los algoritmos de busqueda por fuerza bruta, posterior a eso hay dos celdas que comparan los tiempos de ejecucion de busqueda de vecinos cercanos y de busqueda por radio implementando busqueda con arbol kd y busqueda con fuerza bruta. abajo de cada celda de comparacion se encuentran las conclusiones de cada experimento basado en los resultados obtenidos. Para usar este archivo se deben ejecutar todas las celdas en orden, si se quieren verificar tiempos diferentes se deben cambiar la cantidad de los datos en la primera celda y los parámetros de las funciones. NOTA: para la comparación de tiempos se usa un promedio de tiempos de ejecucion.