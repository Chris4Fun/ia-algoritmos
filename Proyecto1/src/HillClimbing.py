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

# Hill Climbing para resolver el problema del viajero
def hill_climbing_viajero(agente, ciudades):
    mejor_entregas = viajero.evaluar_ruta(agente, ciudades)
    print(f"Entregas iniciales: {mejor_entregas}")
    
    while True:
        nuevas_rutas = viajero.cambios_ruta(ciudades)

        entregas = []
        for ruta in nuevas_rutas:
            nuevas_entregas = viajero.evaluar_ruta(agente, ruta)
            entregas.append(nuevas_entregas)
        
        max_entregas = max(entregas)
        max_ruta = nuevas_rutas[entregas.index(max_entregas)]

        if max_entregas > mejor_entregas:
                mejor_entregas = max_entregas
                ciudades = max_ruta
        else:
            break

    return ciudades, mejor_entregas

# Hill Climbing para resolver el problema de distribución
def hill_climbing_n_distribucion(tiempos_maquina_1, tiempos_maquina_2):
    asignacion_actual = dist.primera_asignacion(tiempos_maquina_1, tiempos_maquina_2)
    tiempo_actual = dist.calcular_tiempos(asignacion_actual, tiempos_maquina_1, tiempos_maquina_2)

    while True:
        cambios = dist.cambios_asignacion(asignacion_actual)
        
        tiempos = []
        for vecino in cambios:
            nuevo_tiempo = dist.calcular_tiempos(vecino, tiempos_maquina_1, tiempos_maquina_2)
            tiempos.append(nuevo_tiempo)
        
        mejor_tiempo = min(tiempos)
        mejor_asignacion = cambios[tiempos.index(mejor_tiempo)]

        if mejor_tiempo < tiempo_actual:
            tiempo_actual = mejor_tiempo
            asignacion_actual = mejor_asignacion
        else:
            break
    
    return tiempo_actual, asignacion_actual


def n_reinas(n):
    # Tablero inicial aleatorio
    tablero = list(range(n))
    random.shuffle(tablero)
    # Hill Climbing
    solucion, conflictos = hill_climbing_n_reinas(tablero)
    print("\nSolución final:")
    reinas.imprimir_tablero(solucion)

def n_distribucion(tiempos_maquina_1, tiempos_maquina_2):
    tiempo, asignacion = hill_climbing_n_distribucion(tiempos_maquina_1, tiempos_maquina_2)
    print("\nSolución final:")
    dist.imprimir(asignacion, tiempos_maquina_1, tiempos_maquina_2)

def n_viajero(agente, ciudades):
    mejor_ruta, mejor_entregas = hill_climbing_viajero(agente, ciudades)
    print("\nSolución final:")
    viajero.imprimir(mejor_ruta, mejor_entregas)

ciudades = [
    viajero.Ciudad("A", "recolectar", suministra = 10),
    viajero.Ciudad("B", "entregar", demanda = 5),
    viajero.Ciudad("C", "recolectar", suministra = 7),
    viajero.Ciudad("D", "entregar", demanda = 8),
    viajero.Ciudad("E", "entregar", demanda = 6),
]
# Create an agent with a max capacity of 15
agente = viajero.Viajero(capacidad = 15)

tiempos_maquina_1 = [2, 6, 3, 4, 2]
tiempos_maquina_2 = [7, 2, 5, 3, 6]

n_viajero(agente, ciudades)
n_distribucion(tiempos_maquina_1, tiempos_maquina_2)
n_reinas(8)