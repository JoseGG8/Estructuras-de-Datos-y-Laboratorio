# Laboratorio de Seguridad: Hashes y Árboles de Merkle

Este laboratorio práctico, desarrollado en Python, explora el uso de funciones de hash criptográficas y estructuras de datos para la validación de integridad.

---

## 1. Búsqueda de Preimagen (Fuerza Bruta)
Este programa está diseñado para encontrar la entrada original (preimagen) de un hash **SHA-256** cuando se sabe que la fuente es una secuencia numérica de **10 dígitos**.

### Instrucciones de uso:
1. **Ejecución:** Inicia el script del "Punto #1".
2. **Entrada:** Introduce el hash hexadecimal objetivo cuando el sistema lo solicite.
3. **Proceso:** El algoritmo utiliza la librería `itertools` para generar todas las combinaciones posibles desde `0000000000` hasta `9999999999`.
4. **Salida:** * Si el hash coincide con alguna combinación, el programa imprimirá la **secuencia de 10 números** exacta.
   * Si no hay coincidencia, se informará que la secuencia no fue encontrada.

---

## 2. Recuperación de Orden con Árbol de Merkle
Este programa utiliza la estructura de un Árbol de Merkle para determinar el orden original de un conjunto de transacciones basándose en un hash raíz (Merkle Root) de referencia.

### Componentes Técnicos:
* **Clase `Nodo`:** Almacena el valor hash y mantiene una referencia a su nodo "pareja" o hermano para poder escalar en el árbol.
* **Clase `MerkleArbol`:** Gestiona la creación de hashes iniciales, el balanceo del árbol (duplicando nodos si la cantidad es impar) y el cálculo iterativo hasta llegar a la raíz.

### Instrucciones de uso:
1. **Referencia:** El sistema establece un **Root de referencia** a partir de una lista de transacciones predefinida.
2. **Entrada:** Escribe las transacciones que conoces separadas por comas (ejemplo: `hola1, hola2, hola3, hola4`).
3. **Búsqueda:** El script genera todas las permutaciones posibles del orden de esas palabras.
4. **Validación:** El programa reconstruye un árbol para cada orden posible y lo compara con la raíz original.
5. **Resultado:** Una vez encontrada la coincidencia, el script despliega el **orden correcto** de las transacciones.

---

## Requisitos
Para ejecutar estos programas, asegúrate de tener instalado **Python 3.x** y las siguientes librerías estándar:
* `hashlib`
* `itertools`
* `random`
