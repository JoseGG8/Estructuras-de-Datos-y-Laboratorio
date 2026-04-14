import matplotlib.pyplot as plt
import numpy as np

def graficar_busqueda_radio(arbol, punto_objetivo, radio):
    """
    Args:
        arbol: instancia de KD_Tree ya construida.
        punto_objetivo (tuple): Tupla (x, y).
        radio (float): Valor numérico del radio de búsqueda.
    """
    # 1. Obtener los puntos que están dentro del radio usando tu método del árbol
    puntos_dentro = arbol.buscar_por_radio(punto_objetivo, radio)
    
    # 2. Separar todos los puntos originales para el fondo
    todos_x = [p[0] for p in arbol.datos]
    todos_y = [p[1] for p in arbol.datos]
    
    # 3. Separar los puntos encontrados para resaltarlos
    dentro_x = [p[0] for p in puntos_dentro]
    dentro_y = [p[1] for p in puntos_dentro]

    plt.figure(figsize=(10, 10))

    # Graficar todos los puntos (delgados y grises)
    plt.scatter(todos_x, todos_y, s=1, marker=',', color='lightgray', alpha=0.4, label='Puntos fuera')

    # Graficar puntos dentro del radio (un poco más grandes y rojos)
    plt.scatter(dentro_x, dentro_y, s=5, marker='o', color='red', label=f'Dentro del radio ({len(puntos_dentro)} puntos)')

    # Graficar el punto objetivo (el centro) con una 'X' azul
    plt.scatter(punto_objetivo[0], punto_objetivo[1], s=50, marker='X', color='blue', label='Objetivo')

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
    Args:
        arbol: instancia de KD_Tree ya construida.
        punto_objetivo: tupla (x,y) del punto a buscarle un vecino
    """
    # 1. Usar tu método para encontrar el vecino
    vecino_coordenadas = arbol.buscar_vecino_cercano(punto_objetivo)
    
    if vecino_coordenadas is None:
        print("El árbol está vacío o no se encontró vecino.")
        return

    # Crear la figura (cuadrada para no deformar distancias)
    fig, ax = plt.subplots(figsize=(9, 9))

    # ==========================================================
    # CAPA 1: Definir el Zoom (Protagonistas)
    # ==========================================================
    # Graficamos PRIMERO los puntos que queremos que definan el zoom.
    
    # Punto Objetivo (X azul grande)
    ax.scatter(punto_objetivo[0], punto_objetivo[1], s=250, marker='X', 
               color='blue', label='Objetivo (Tú)', zorder=10)
    
    # Vecino Encontrado (Círculo rojo grueso y vacío)
    ax.scatter(vecino_coordenadas[0], vecino_coordenadas[1], s=350, 
               facecolors='none', edgecolors='red', linewidths=3.5, 
               label='Vecino Más Cercano', zorder=11)

    # Línea punteada que une los dos puntos (resalta la distancia)
    ax.plot([punto_objetivo[0], vecino_coordenadas[0]], 
            [punto_objetivo[1], vecino_coordenadas[1]], 
            linestyle='--', color='red', alpha=0.6, zorder=5)

    # --- EL TRUCO DEL ZOOM RELATIVO ---
    # Añadimos un margen del 50% (0.5) alrededor de estos dos puntos.
    # Esto asegura que se vean cerca pero con aire alrededor.
    ax.margins(0.5) 

    # ==========================================================
    # CAPA 2: Contexto (Puntos que NO son el vecino)
    # ==========================================================
    # CRÍTICO: Desactivamos el autoescalado para que estos puntos
    # aparezcan pero NO alejen la cámara.
    ax.set_autoscale_on(False) 

    # Extraemos todos los puntos originales del árbol
    todos_x = [p[0] for p in arbol.datos]
    todos_y = [p[1] for p in arbol.datos]
    
    # Graficamos el fondo: muy pequeños, grises y con alta transparencia
    ax.scatter(todos_x, todos_y, s=12, marker=',', color='gray', 
               alpha=0.5, label='Puntos de Contexto', zorder=1)

    # Estética final
    ax.set_title(f"Detalle de Vecindad: Objetivo vs Vecino\nCentrado en {punto_objetivo}", fontsize=14)
    ax.legend(loc='upper right', fontsize=10)
    ax.grid(True, linestyle=':', alpha=0.4)
    
    # Asegura que 1 unidad en X sea igual a 1 unidad en Y
    ax.set_aspect('equal', adjustable='datalim')
    
    plt.tight_layout()
    plt.show()
