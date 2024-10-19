import Distribucion as dist
import NReinas as reinas
import Viajero as viajero
import random

# Hill Climbing para resolver el problema de las n reinas
def hill_climbing_n_reinas(tablero):
    n = len(tablero)
    costo = reinas.conflictos(tablero)
    
    print("Tablero inicial:")
    reinas.imprimir_tablero(tablero)

    while True:
        movimientos = reinas.movimientos(tablero)

        mejor_movimiento = []
        costo_movimiento = n*n
        # Buscar el mejor movimiento
        for movimiento in movimientos:
            nuevo_costo = reinas.conflictos(movimiento)
            if (nuevo_costo < costo_movimiento):
                mejor_movimiento = movimiento
                costo_movimiento = nuevo_costo

        # Si el mejor movimiento es mejor que la solucion actual, se actualiza
        if costo_movimiento < costo:
            tablero, costo = mejor_movimiento, costo_movimiento
        else:
            break
    
    return tablero, costo

# Hill Climbing para resolver el problema de las n reinas
def hill_climbing_viajero():
    pass

# Hill Climbing para resolver el problema de las n reinas
def hill_climbing_n_distribucion():
    pass

def n_reinas(n):
    # Tablero inicial aleatorio
    tablero = list(range(n))
    random.shuffle(tablero)
    # Hill Climbing
    solucion, conflictos = hill_climbing_n_reinas(tablero)
    print("\nSolución final:")
    reinas.imprimir_tablero(solucion)

n_reinas(8)
