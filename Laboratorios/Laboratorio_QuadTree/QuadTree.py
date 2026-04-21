import math

class Nodo_Hoja():
    def __init__(self, coordenada):
        self.coordenada = coordenada
        self.padre = None

class Nodo_intermedio():
    def __init__(self, datos, num_hijos):
        self.datos = datos
        self.padre = None
        self.hijos = [None] * num_hijos

class QuadTree():
    def __init__(self, datos, dimensiones):
        self.datos = datos
        self.dimensiones = dimensiones
        self.root = None

    def mitad_datos(self, datos):
        punto_medio = []
        for i in range(self.dimensiones):
            min_val = min(datos, key=lambda c: c[i])[i]-10
            max_val = max(datos, key=lambda c: c[i])[i]+10
            # Usamos suma para encontrar el centro de la caja
            punto_medio.append((min_val + max_val) / 2)
        return punto_medio

    def particionar_listas(self, datos):
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
        num_hijos = 2**self.dimensiones

        # 1. Manejo de la Raíz
        if nodo is None:
            self.root = Nodo_intermedio(self.datos, num_hijos)
            nodo_actual = self.root
        else:
            nodo_actual = nodo

        # 2. Particionamos los datos del nodo actual
        listas_datos_hijos = self.particionar_listas(nodo_actual.datos)

        # 3. Creamos los nodos hijos
        for i, datos_hijo in enumerate(listas_datos_hijos):
            if len(datos_hijo) > 1:
                # Nodo intermedio: Crear y seguir construyendo
                nuevo_nodo = Nodo_intermedio(datos_hijo, num_hijos)
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
        self.mejor_punto = None
        self.mejor_distancia = float('inf')
        # Iniciamos la recursión pasando la raíz y sus datos para calcular límites
        self._nns_recursivo(self.root, punto_Q)
        return self.mejor_punto, self.mejor_distancia

    def _nns_recursivo(self, nodo, punto_Q):
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
        centro = self.mitad_datos(nodo.datos)

        # 1. Bajada inicial (determinar el hijo más probable)
        indice_prometedor = 0
        for i in range(self.dimensiones):
            if punto_Q[i] >= centro[i]:
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
            datos_hijo = [nodo_hijo.coordenada]
        else:
            datos_hijo = nodo_hijo.datos

        # Calculamos límites (AABB) al vuelo
        dist_cuadrada = 0
        for i in range(self.dimensiones):
            min_eje = min(datos_hijo, key=lambda c: c[i])[i]
            max_eje = max(datos_hijo, key=lambda c: c[i])[i]

            if punto_Q[i] < min_eje:
                dist_cuadrada += (min_eje - punto_Q[i]) ** 2
            elif punto_Q[i] > max_eje:
                dist_cuadrada += (punto_Q[i] - max_eje - punto_Q[i]) ** 2

        return math.sqrt(dist_cuadrada) < self.mejor_distancia

    def calcular_distancia(self, p1, p2):
        return math.sqrt(sum((a - b)**2 for a, b in zip(p1, p2)))

    def buscar_por_radio(self, punto_Q, radio):
        self.puntos_encontrados = []
        self.radio_busqueda = radio
        # Iniciamos la recursión desde la raíz
        self._radio_recursivo(self.root, punto_Q)
        return self.puntos_encontrados

    def _radio_recursivo(self, nodo, punto_Q):
        if nodo is None:
            return

        # CASO HOJA: Verificamos si el punto individual está dentro del radio
        if isinstance(nodo, Nodo_Hoja):
            dist = self.calcular_distancia(punto_Q, nodo.coordenada)
            if dist <= self.radio_busqueda:
                self.puntos_encontrados.append(nodo.coordenada)
            return

        # CASO NODO INTERMEDIO
        # 1. Verificamos si vale la pena revisar este nodo y sus hijos
        # Comprobamos la distancia entre Q y la "caja" de este nodo
        if self._caja_dentro_de_radio(punto_Q, nodo):
            # Si hay intersección, revisamos a todos sus hijos
            for hijo in nodo.hijos:
                self._radio_recursivo(hijo, punto_Q)

    def _caja_dentro_de_radio(self, punto_Q, nodo):
        """
        Calcula la distancia mínima desde el punto Q hasta la caja (AABB)
        formada por los datos del nodo.
        """
        # Obtenemos los límites de los datos en este nodo
        datos_nodo = nodo.datos

        dist_cuadrada = 0
        for i in range(self.dimensiones):
            min_val = min(datos_nodo, key=lambda c: c[i])[i]
            max_val = max(datos_nodo, key=lambda c: c[i])[i]

            # Calculamos la distancia al borde de la caja en cada eje
            if punto_Q[i] < min_val:
                dist_cuadrada += (min_val - punto_Q[i]) ** 2
            elif punto_Q[i] > max_val:
                dist_cuadrada += (punto_Q[i] - max_val) ** 2

        # Si la distancia mínima a la caja es menor o igual al radio, hay intersección
        return math.sqrt(dist_cuadrada) <= self.radio_busqueda




