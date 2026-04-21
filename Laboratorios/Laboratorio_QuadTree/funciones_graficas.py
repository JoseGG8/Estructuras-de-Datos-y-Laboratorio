import matplotlib.pyplot as plt
import numpy as np
from QuadTree import *
import time

def graficar_busqueda_radio(arbol, punto_objetivo, radio):
    """
    Visualiza todos los puntos que estan dentro de un radio definido tomado a partir del punto objetivo
    Args:
        arbol: instancia de QuadTree ya construida.
        punto_objetivo (tuple): Tupla (x, y).
        radio (float): Valor numérico del radio de búsqueda.
    """
    # 1. Obtener los puntos que están dentro del radio usando tu método del árbol
    puntos_dentro = arbol.buscar_por_radio(punto_objetivo, radio)
    
    # 2. Separar todos los puntos originales para el fondo
    todos_x = [p[0] for p in arbol.datos]
    todos_y = [p[1] for p in arbol.datos]
    
    # 3. Separar los puntos encontrados para resaltarlos
    dentro_x = [p[0] for p in puntos_dentro[0]]
    dentro_y = [p[1] for p in puntos_dentro[0]]

    cercanos_x = [p[0] for p in puntos_dentro[1]]
    cercanos_y = [p[1] for p in puntos_dentro[1]]

    plt.figure(figsize=(10, 10))

    # Graficar todos los puntos (delgados y grises)
    plt.scatter(todos_x, todos_y, s=1, marker=',', color='lightgray', alpha=0.4, label='Puntos fuera')

    # Graficar puntos dentro del radio (un poco más grandes y rojos)
    plt.scatter(dentro_x, dentro_y, s=5, marker='o', color='red', label=f'Dentro del radio ({len(puntos_dentro[0])} puntos)')

    # Graficar el punto objetivo (el centro) con una 'X' azul
    plt.scatter(punto_objetivo[0], punto_objetivo[1], s=50, marker='X', color='blue', label='Objetivo')

    #Graficar 5 puntos más cercanos
    plt.scatter(cercanos_x, cercanos_y, s=5, marker='o', color='yellow', label=f'20 puntos más cercanos ({len(puntos_dentro[1])} puntos)')


    # Dibujar el círculo del radio para visualizar el límite
    circulo = plt.Circle(punto_objetivo, radio, color='blue', fill=False, linestyle='--', alpha=0.5)
    plt.gca().add_patch(circulo)

    # Estética
    plt.title(f"Búsqueda por Radio: {radio} unidades")
    plt.legend(loc='upper right')
    plt.axis('equal')
    plt.grid(True, linestyle=':', alpha=0.6)
    
    plt.show()


def graficar_vecino_cercano(arbol, punto_objetivo):
    """
    Visualiza el vecino más cercano con un zoom inteligente que destaca
    a los protagonistas y mantiene el resto de puntos como contexto Tenue.
    """
    # 1. Usar tu método para encontrar el vecino
    # IMPORTANTE: Desempaquetamos la tupla (coordenada, distancia)
    resultado = arbol.buscar_vecino_cercano(punto_objetivo)
    
    if resultado[0] is None:
        print("El árbol está vacío o no se encontró vecino.")
        return

    # Separamos la coordenada de la distancia para graficar
    vecino_coordenadas, dist_encontrada = resultado

    # Crear la figura (cuadrada para no deformar distancias)
    fig, ax = plt.subplots(figsize=(9, 9))

    # ==========================================================
    # CAPA 1: Definir el Zoom (Protagonistas)
    # ==========================================================
    
    # Punto Objetivo (X azul grande)
    ax.scatter(punto_objetivo[0], punto_objetivo[1], s=250, marker='X', 
               color='blue', label='Objetivo (Tú)', zorder=10)
    
    # Vecino Encontrado (Círculo rojo grueso y vacío)
    ax.scatter(vecino_coordenadas[0], vecino_coordenadas[1], s=350, 
               facecolors='none', edgecolors='red', linewidths=3.5, 
               label=f'Vecino Más Cercano (dist: {dist_encontrada:.2f})', zorder=11)

    # Línea punteada que une los dos puntos
    ax.plot([punto_objetivo[0], vecino_coordenadas[0]], 
            [punto_objetivo[1], vecino_coordenadas[1]], 
            linestyle='--', color='red', alpha=0.6, zorder=5)

    # Margen para que se vea aire alrededor de los dos puntos principales
    ax.margins(0.5) 

    # ==========================================================
    # CAPA 2: Contexto (Puntos que NO son el vecino)
    # ==========================================================
    # Desactivamos el autoescalado para mantener el zoom en el objetivo y vecino
    ax.set_autoscale_on(False) 

    todos_x = [p[0] for p in arbol.datos]
    todos_y = [p[1] for p in arbol.datos]
    
    # Graficamos el fondo tenue
    ax.scatter(todos_x, todos_y, s=12, marker=',', color='gray', 
               alpha=0.3, label='Puntos de Contexto', zorder=1)

    # Estética final
    ax.set_title(f"Búsqueda NNS en QuadTree\nObjetivo: {punto_objetivo}", fontsize=14)
    ax.legend(loc='upper right', fontsize=10)
    ax.grid(True, linestyle=':', alpha=0.4)
    
    ax.set_aspect('equal', adjustable='datalim')
    
    plt.tight_layout()
    plt.show()

def graficar_comparativa(resultados):
    """
    Recibe el diccionario de la función anterior y genera las gráficas.
    """
    n = resultados['n']
    
    plt.figure(figsize=(14, 6))

    # Gráfica 1: Vecino Cercano
    plt.subplot(1, 2, 1)
    plt.plot(n, resultados['nn_fb'], 'o--', label='Fuerza Bruta', color='#e74c3c', linewidth=2)
    plt.plot(n, resultados['nn_kd'], 's-', label='QuadTree', color='#3498db', linewidth=2)
    plt.title('Rendimiento: Vecino Más Cercano', fontsize=14)
    plt.xlabel('Cantidad de Puntos (N)')
    plt.ylabel('Tiempo (segundos)')
    plt.legend()
    plt.grid(True, alpha=0.3)

    # Gráfica 2: Búsqueda por Radio
    plt.subplot(1, 2, 2)
    plt.plot(n, resultados['radio_fb'], 'o--', label='Fuerza Bruta', color='#f39c12', linewidth=2)
    plt.plot(n, resultados['radio_kd'], 's-', label='QuadTree', color='#2ecc71', linewidth=2)
    plt.title('Rendimiento: Búsqueda por Radio', fontsize=14)
    plt.xlabel('Cantidad de Puntos (N)')
    plt.ylabel('Tiempo (segundos)')
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

def graficar_rendimiento_por_radio(arbol, punto_Q, radios_lista):
    """
    Mide y grafica cómo varía el tiempo de búsqueda según el tamaño del radio.
    
    Args:
        arbol: El QuadTree ya construido.
        punto_Q: Punto central para las búsquedas.
        radios_lista: Lista de radios a probar (ej. [1, 5, 10, 20, 50, 100...])
    """
    tiempos = []
    cantidades_puntos = []

    for r in radios_lista:
        # Medimos el tiempo de la búsqueda por radio
        inicio = time.time()
        puntos, _ = arbol.buscar_por_radio(punto_Q, r)
        fin = time.time()
        
        tiempos.append(fin - inicio)
        cantidades_puntos.append(len(puntos))

    # Crear la gráfica
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Eje principal: Tiempos
    color_tiempo = '#2ecc71'
    ax1.set_xlabel('Radio de Búsqueda')
    ax1.set_ylabel('Tiempo de ejecución (segundos)', color=color_tiempo)
    ax1.plot(radios_lista, tiempos, marker='s', linestyle='-', color=color_tiempo, linewidth=2, label='Tiempo QuadTree')
    ax1.tick_params(axis='y', labelcolor=color_tiempo)
    ax1.grid(True, alpha=0.3)


    plt.title(f'Rendimiento de Búsqueda por Radio\n(Punto Central: {punto_Q})', fontsize=14)
    fig.tight_layout()
    plt.show()