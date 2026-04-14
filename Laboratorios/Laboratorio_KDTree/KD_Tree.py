import math

class Nodo():
    """Objeto responsable de almacenar la informacion de las coordenadas y los punteros hacia los demás nodos"""
    def __init__(self, coordenadas):
        self.padre = None
        self.hijo_izquierda = None
        self.hijo_derecha = None
        self.coordenadas = coordenadas


class KD_Tree():
    """Un objeto de esta clase almacena Nodos en una estructura KD_TREE """
    def __init__(self, datos):
        self.root = None
        self.datos = datos

    def mediana_coordenada(self, lista, eje='x'):
        """"En base a una lista y un eje retorna la mediana de los datos según el eje que esté en el argumento y la lista de datos organizada"""
        idx = 0 if eje == 'x' else 1
        ordenada = sorted(lista, key=lambda p: p[idx])
        n = len(ordenada)
        return ordenada[n // 2], ordenada

    def construir_arbol(self, datos=None, node=None, eje='x'):
        """Se encarga de construir el árbol recursivamente """
        if datos is None:
            datos = self.datos

        # 1. caso base
        if not datos:
            return None

        # 2. crear raíz si es primera llamada
        if node is None:
            coordenada, datos_ordenados = self.mediana_coordenada(datos, eje)
            node = Nodo(coordenada)
            self.root = node
        else:
            datos_ordenados = sorted(datos, key=lambda p: p[0] if eje == 'x' else p[1])

        # 3. encontrar mediana
        mid = len(datos_ordenados) // 2
        node.coordenadas = datos_ordenados[mid]

        # 4. dividir
        izquierda = datos_ordenados[:mid]
        derecha = datos_ordenados[mid+1:]

        # 5. siguiente eje
        nuevo_eje = 'y' if eje == 'x' else 'x'

        # 6. construir izquierda
        if izquierda:
            node.hijo_izquierda = Nodo(None)
            node.hijo_izquierda.padre = node
            self.construir_arbol(izquierda, node.hijo_izquierda, nuevo_eje)

        # 7. construir derecha
        if derecha:
            node.hijo_derecha = Nodo(None)
            node.hijo_derecha.padre = node
            self.construir_arbol(derecha, node.hijo_derecha, nuevo_eje)

        return node

    def distancia_cuadrada(self, p1, p2):
        """Calcula la distancia entre dos puntos (sin raíz para que sea más rápido)"""
        return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

    def buscar_vecino_cercano(self, punto_objetivo):
        """Método principal para iniciar la búsqueda"""
        if self.root is None:
            return None
        
        mejor_nodo, mejor_dist = self._nn_recursivo(
            nodo_actual=self.root, 
            objetivo=punto_objetivo, 
            eje='x', 
            mejor_nodo=None, 
            mejor_dist=float('inf')
        )
        return mejor_nodo.coordenadas

    def _nn_recursivo(self, nodo_actual, objetivo, eje, mejor_nodo, mejor_dist):
        if nodo_actual is None or nodo_actual.coordenadas is None:
            return mejor_nodo, mejor_dist

        # 1. Distancia del punto actual al objetivo
        dist_actual = self.distancia_cuadrada(nodo_actual.coordenadas, objetivo)

        if dist_actual < mejor_dist:
            mejor_dist = dist_actual
            mejor_nodo = nodo_actual

        # 2. Eje actual y siguiente
        idx = 0 if eje == 'x' else 1
        nuevo_eje = 'y' if eje == 'x' else 'x'

        # 3. Viaje de ida (bajada lógica)
        if objetivo[idx] < nodo_actual.coordenadas[idx]:
            proximo = nodo_actual.hijo_izquierda
            otro = nodo_actual.hijo_derecha
        else:
            proximo = nodo_actual.hijo_derecha
            otro = nodo_actual.hijo_izquierda

        mejor_nodo, mejor_dist = self._nn_recursivo(proximo, objetivo, nuevo_eje, mejor_nodo, mejor_dist)

        # 4. Backtracking (¿Hay algo mejor al otro lado?)
        distancia_a_la_linea = (objetivo[idx] - nodo_actual.coordenadas[idx])**2

        if distancia_a_la_linea < mejor_dist:
            mejor_nodo, mejor_dist = self._nn_recursivo(otro, objetivo, nuevo_eje, mejor_nodo, mejor_dist)

        return mejor_nodo, mejor_dist
    

    def buscar_por_radio(self, punto_objetivo, radio):
      """Retorna una lista con todos los puntos dentro del radio"""
      resultados = []
      # Usamos el radio al cuadrado para comparar más rápido (evitamos math.sqrt)
      radio_cuadrado = radio ** 2
      
      self._radio_recursivo(self.root, punto_objetivo, 'x', radio_cuadrado, resultados)
      return resultados

    def _radio_recursivo(self, nodo_actual, objetivo, eje, radio_cuadrado, resultados):
      if nodo_actual is None or nodo_actual.coordenadas is None:
          return

      # 1. ¿Este punto está dentro del círculo?
      dist_actual = self.distancia_cuadrada(nodo_actual.coordenadas, objetivo)
      if dist_actual <= radio_cuadrado:
          resultados.append(nodo_actual.coordenadas)

      # 2. Eje actual y siguiente
      idx = 0 if eje == 'x' else 1
      nuevo_eje = 'y' if eje == 'x' else 'x'

      # 3. Decidir qué lado explorar primero (el más lógico)
      if objetivo[idx] < nodo_actual.coordenadas[idx]:
          proximo = nodo_actual.hijo_izquierda
          otro = nodo_actual.hijo_derecha
      else:
          proximo = nodo_actual.hijo_derecha
          otro = nodo_actual.hijo_izquierda

      # Explorar el lado donde está el objetivo
      self._radio_recursivo(proximo, objetivo, nuevo_eje, radio_cuadrado, resultados)

      # 4. ¿El círculo cruza al otro lado?
      # Calculamos la distancia perpendicular a la línea divisoria
      distancia_a_la_linea = (objetivo[idx] - nodo_actual.coordenadas[idx])**2

      if distancia_a_la_linea <= radio_cuadrado:
          # El círculo es tan grande que toca el otro lado, hay que revisar
          self._radio_recursivo(otro, objetivo, nuevo_eje, radio_cuadrado, resultados)
    
