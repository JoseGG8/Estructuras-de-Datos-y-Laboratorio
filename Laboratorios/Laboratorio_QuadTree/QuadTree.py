import math

class Nodo_Hoja():
    def __init__(self, coordenada):
        self.coordenada = coordenada
        self.padre = None

class Nodo_intermedio():
    def __init__(self, datos, centro, mins, maxs, num_hijos):
        self.datos = datos
        self.centro = centro ##centro del cuadrante
        self.mins = mins  ##limite superior
        self.maxs = maxs  ##limite inferior
        self.padre = None
        self.hijos = [None] * num_hijos

class QuadTree():
    
    def __init__(self, datos, dimensiones):
        """Constructor de la clase quadTree.
        Args:
        datos (list(tuple)): lista de tuplas de datos coordenados,
        dimensiones (int): dimensiones de los datos"""
        self.datos = datos
        self.dimensiones = dimensiones
        self.root = None

    def mitad_datos(self, datos):
        """Se encarga de calcular cual es el punto medio. Este método se utiliza en el método particionar listas
        Args:
            datos (list): Lista de datos coordenados (x,y,z,...)"""
        punto_medio = []
        for i in range(self.dimensiones):
            min_val = min(datos, key=lambda c: c[i])[i]
            max_val = max(datos, key=lambda c: c[i])[i]
            # Usamos suma para encontrar el centro de la caja
            punto_medio.append((min_val + max_val) / 2)
        return punto_medio

    def particionar_listas(self, datos):
        """Método encargado de dividir los datos que se le pasan como argumento en 2**dimensiones.
        Utiliza lógica de bits en un numero binario para ubicar cada lista en su cuadrante/octante respectivo, ejemplo:
        si el punto (x1,y1) es menor que (xmedio, ymedio) en todas sus coordenadas, el numero binario es 00, con 00 se va al cuadrante inferior izquerdo"""
        punto_medio = self.mitad_datos(datos)
        num_hijos = 2**self.dimensiones
        listas_hijos = [[] for _ in range(num_hijos)]

        for punto in datos:
            indice_hijo = 0
            for i in range(self.dimensiones):
                if punto[i] >= punto_medio[i]:
                    indice_hijo |= (1 << i)
            listas_hijos[indice_hijo].append(punto)

        return listas_hijos

    def construir_arbol(self, nodo=None):
        """Método encargado de construir el arbol recursivamente"""
        num_hijos = 2**self.dimensiones

        # 1. Manejo de la Raíz
        if nodo is None:
            mins = [min(self.datos, key=lambda c: c[i])[i] for i in range(self.dimensiones)]
            maxs = [max(self.datos, key=lambda c: c[i])[i] for i in range(self.dimensiones)]
            centro = self.mitad_datos(self.datos)

            self.root = Nodo_intermedio(self.datos,centro, mins, maxs, num_hijos)
            nodo_actual = self.root
        else:
            nodo_actual = nodo

        # 2. Particionamos los datos del nodo actual
        listas_datos_hijos = self.particionar_listas(nodo_actual.datos)

        # 3. Creamos los nodos hijos
        for i, datos_hijo in enumerate(listas_datos_hijos):
            if len(datos_hijo) > 1:
                
                #si todos los puntos son iguales  no podemos seguir dividiendo, recursion infinita#
                if all(p == datos_hijo[0] for p in datos_hijo):
                    nuevo_nodo = Nodo_Hoja(datos_hijo[0])
                    nuevo_nodo.padre = nodo_actual
                    nodo_actual.hijos[i] = nuevo_nodo
                    continue
                # Nodo intermedio: Crear y seguir construyendo
                hijo_mins = [min(datos_hijo, key=lambda c: c[j])[j] for j in range(self.dimensiones)]
                hijo_maxs = [max(datos_hijo, key=lambda c: c[j])[j] for j in range(self.dimensiones)]
                hijo_centro = self.mitad_datos(datos_hijo)

                nuevo_nodo = Nodo_intermedio(datos_hijo,hijo_centro,hijo_mins,hijo_maxs, num_hijos)
                nuevo_nodo.padre = nodo_actual
                nodo_actual.hijos[i] = nuevo_nodo
                self.construir_arbol(nuevo_nodo)

            elif len(datos_hijo) == 1:
                # Nodo hoja: Punto final
                nuevo_nodo = Nodo_Hoja(datos_hijo[0])
                nuevo_nodo.padre = nodo_actual
                nodo_actual.hijos[i] = nuevo_nodo

            else:
                # Espacio vacío
                nodo_actual.hijos[i] = None

    def buscar_vecino_cercano(self, punto_Q):
        """Método principal para la busca de un vecino cercano con un punto de referencia
        Args: 
        punto_Q (tuple): coordenada"""
        self.mejor_punto = None
        self.mejor_distancia = float('inf')
        # Iniciamos la recursión pasando la raíz y sus datos para calcular límites
        self._nns_recursivo(self.root, punto_Q)
        return self.mejor_punto, self.mejor_distancia

    def _nns_recursivo(self, nodo, punto_Q):
        """Se encarga de bajar hasta un nodo hoja guiandose por el centro del cuadrante actual, cuando encuentra una hoja deja un mejor candidato.
        Después de bajar se hace una poda"""
        if nodo is None:
            return

        # CASO HOJA
        if isinstance(nodo, Nodo_Hoja):
            dist = self.calcular_distancia(punto_Q, nodo.coordenada)
            if dist < self.mejor_distancia:
                self.mejor_distancia = dist
                self.mejor_punto = nodo.coordenada
            return

        # CASO NODO INTERMEDIO

        # 1. Bajada inicial (determinar el hijo más probable)
        indice_prometedor = 0
        for i in range(self.dimensiones):
            if punto_Q[i] >= nodo.centro[i]:
                indice_prometedor |= (1 << i)

        # 2. Explorar primero el hijo donde "cae" Q
        self._nns_recursivo(nodo.hijos[indice_prometedor], punto_Q)

        # 3. Revisar hermanos
        for i, hijo in enumerate(nodo.hijos):
            if hijo is not None and i != indice_prometedor:
                # Calculamos los límites de este hijo para decidir si entrar
                if self._verificar_poda_sin_datos(punto_Q, hijo):
                    self._nns_recursivo(hijo, punto_Q)

    def _verificar_poda_sin_datos(self, punto_Q, nodo_hijo):
        """
        Calcula si la caja que contiene los datos del hijo está
        dentro del radio de nuestra mejor distancia actual.
        """
        # Obtenemos los datos que viven en ese hijo
        datos_hijo = []
        if isinstance(nodo_hijo, Nodo_Hoja):
            dist_hoja = self.calcular_distancia(punto_Q, nodo_hijo.coordenada)
            return dist_hoja < self.mejor_distancia

        # Calculamos límites 
        dist_cuadrada = 0
        for i in range(self.dimensiones):

            if punto_Q[i] < nodo_hijo.mins[i]:
                dist_cuadrada += (nodo_hijo.mins[i] - punto_Q[i]) ** 2
            elif punto_Q[i] > nodo_hijo.maxs[i]:
                dist_cuadrada += (punto_Q[i] - nodo_hijo.maxs[i]) ** 2

        return math.sqrt(dist_cuadrada) < self.mejor_distancia

    def calcular_distancia(self, p1, p2):
        return math.sqrt(sum((a - b)**2 for a, b in zip(p1, p2)))

    def buscar_por_radio(self, punto_Q, radio):
        # Usamos una lista temporal para guardar (punto, distancia)
        self._resultados_temporales = []
        self.radio_busqueda = radio
        
        # Iniciamos la recursión desde la raíz
        self._radio_recursivo(self.root, punto_Q)
        
        # 1. Ordenamos por distancia (el segundo elemento de la tupla)
        self._resultados_temporales.sort(key=lambda x: x[1])
        
        # 2. Extraemos solo las coordenadas para las listas finales
        todos_los_puntos = [res[0] for res in self._resultados_temporales]
        los_5_mas_cercanos = todos_los_puntos[:5]
        
        return todos_los_puntos, los_5_mas_cercanos

    def _radio_recursivo(self, nodo, punto_Q):
        if nodo is None:
            return

        # CASO HOJA: Verificamos si el punto individual está dentro del radio
        if isinstance(nodo, Nodo_Hoja):
            dist = self.calcular_distancia(punto_Q, nodo.coordenada)
            if dist <= self.radio_busqueda:
                # Guardamos la tupla (coordenada, distancia) para no recalcular luego
                self._resultados_temporales.append((nodo.coordenada, dist))
            return

        # CASO NODO INTERMEDIO
        # 1. Verificamos si vale la pena revisar este nodo y sus hijos
        if self._caja_dentro_de_radio(punto_Q, nodo):
            # Si hay intersección, revisamos a todos sus hijos
            for hijo in nodo.hijos:
                self._radio_recursivo(hijo, punto_Q)

    def _caja_dentro_de_radio(self, punto_Q, nodo):
        """
        Calcula la distancia mínima desde el punto Q hasta la caja (AABB)
        formada por los datos del nodo.
        """
        datos_nodo = nodo.datos
        dist_cuadrada = 0
        
        for i in range(self.dimensiones):
            # Encontramos los límites de este nodo en el eje actual
            # Calculamos la distancia al borde de la caja en cada eje
            if punto_Q[i] < nodo.mins[i]:
                dist_cuadrada += (nodo.mins[i] - punto_Q[i]) ** 2
            elif punto_Q[i] > nodo.maxs[i]:
                dist_cuadrada += (punto_Q[i] - nodo.maxs[i]) ** 2

        # Retornamos True si el radio alcanza a tocar la caja
        return math.sqrt(dist_cuadrada) <= self.radio_busqueda




