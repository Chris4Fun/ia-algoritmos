# Import necessary modules for each problem
import Distribucion as dist
import NReinas as reinas
import Viajero as viajero

import time

# Import each genetic algorithm
from Genetic.GeneticDist import *
from Genetic.GeneticReinas import *
from Genetic.GeneticViaj import *

# Functions used to call each algorithm separately

def n_reinas(n):
    start_time = time.perf_counter()
    mejor_solucion, conflictos = genetic_n_reinas(n)
    end_time = time.perf_counter()
    print("\nSolución final para N-Reinas con algoritmo genético:")
    reinas.imprimir_tablero(mejor_solucion)
    print(f"Conflictos: {conflictos}")
    print("Tiempo de ejecución: {:.8f} s".format(end_time - start_time))

def n_distribucion(tiempos_maquina_1, tiempos_maquina_2):
    start_time = time.perf_counter()
    mejor_solucion, mejor_tiempo = genetic_distribucion(tiempos_maquina_1, tiempos_maquina_2)
    end_time = time.perf_counter()
    print("\nSolución final para Distribución con algoritmo genético:")
    dist.imprimir(mejor_solucion, tiempos_maquina_1, tiempos_maquina_2)
    print(f"Makespan: {mejor_tiempo}")
    print("Tiempo de ejecución: {:.8f} s".format(end_time - start_time))

def n_viajero(agente, ciudades):
    mejor_entregas = viajero.evaluar_ruta(agente, ciudades)
    print(f"Entregas iniciales: {mejor_entregas}")
    start_time = time.perf_counter()
    mejor_ruta, mejor_entregas = genetic_viajero(agente, ciudades)
    end_time = time.perf_counter()
    print("\nSolución final para Viajero con algoritmo genético:")
    viajero.imprimir(mejor_ruta, mejor_entregas)
    print("Tiempo de ejecución: {:.8f} s".format(end_time - start_time))

# Example initialization and usage

ciudades = [
    viajero.Ciudad("A", "recolectar", suministra=10),
    viajero.Ciudad("B", "entregar", demanda=5),
    viajero.Ciudad("C", "recolectar", suministra=7),
    viajero.Ciudad("D", "entregar", demanda=8),
    viajero.Ciudad("E", "entregar", demanda=6),
]

agente = viajero.Viajero(capacidad=15)

# Caso de uso 1
ciudades1 = [
    viajero.Ciudad("A", "recolectar", suministra=10),
    viajero.Ciudad("B", "entregar", demanda=5),
    viajero.Ciudad("C", "recolectar", suministra=7),
    viajero.Ciudad("D", "entregar", demanda=8),
    viajero.Ciudad("E", "entregar", demanda=6),
]
agente1 = viajero.Viajero(capacidad=15)

# Caso de uso 2
ciudades2 = [
    viajero.Ciudad("F", "recolectar", suministra=12),
    viajero.Ciudad("G", "entregar", demanda=4),
    viajero.Ciudad("H", "recolectar", suministra=6),
    viajero.Ciudad("I", "entregar", demanda=10),
    viajero.Ciudad("J", "entregar", demanda=5),
    viajero.Ciudad("K", "recolectar", suministra=8),
]
agente2 = viajero.Viajero(capacidad=18)

# Caso de uso 3
ciudades3 = [
    viajero.Ciudad("L", "recolectar", suministra=9),
    viajero.Ciudad("M", "entregar", demanda=5),
    viajero.Ciudad("N", "entregar", demanda=7),
    viajero.Ciudad("O", "recolectar", suministra=6),
    viajero.Ciudad("P", "entregar", demanda=8),
    viajero.Ciudad("Q", "recolectar", suministra=10),
    viajero.Ciudad("R", "entregar", demanda=4),
]
agente3 = viajero.Viajero(capacidad=20)

# Caso de uso 4
ciudades4 = [
    viajero.Ciudad("Y", "recolectar", suministra=8),
    viajero.Ciudad("Z", "entregar", demanda=6),
    viajero.Ciudad("AA", "recolectar", suministra=10),
    viajero.Ciudad("AB", "entregar", demanda=5),
    viajero.Ciudad("AC", "entregar", demanda=9),
    viajero.Ciudad("AD", "recolectar", suministra=12),
    viajero.Ciudad("AE", "entregar", demanda=4),
    viajero.Ciudad("AF", "recolectar", suministra=6),
]
agente4 = viajero.Viajero(capacidad=30)

ciudades5 = [
    viajero.Ciudad("AG", "recolectar", suministra=10),
    viajero.Ciudad("AH", "entregar", demanda=7),
    viajero.Ciudad("AI", "recolectar", suministra=8),
    viajero.Ciudad("AJ", "entregar", demanda=5),
    viajero.Ciudad("AK", "recolectar", suministra=12),
    viajero.Ciudad("AL", "entregar", demanda=9),
    viajero.Ciudad("AM", "recolectar", suministra=6),
    viajero.Ciudad("AN", "entregar", demanda=4),
    viajero.Ciudad("AO", "recolectar", suministra=7),
    viajero.Ciudad("AP", "entregar", demanda=8),
]
agente5 = viajero.Viajero(capacidad=35)

# Caso Mediano 1 (15 Tareas)
tiempos_maquina_1 = [7, 5, 9, 6, 8, 10, 4, 6, 7, 9, 3, 8, 5, 6, 7]
tiempos_maquina_2 = [5, 8, 6, 7, 4, 5, 9, 6, 10, 3, 7, 4, 8, 6, 5]

# # Caso Mediano 2 (18 Tareas)
# tiempos_maquina_1 = [6, 8, 7, 9, 5, 4, 7, 10, 8, 6, 9, 5, 6, 7, 8, 4, 5, 6]
# tiempos_maquina_2 = [7, 5, 8, 6, 9, 4, 7, 6, 5, 8, 3, 10, 7, 6, 5, 8, 7, 4]

# # Caso Mediano 4 (22 Tareas)
# tiempos_maquina_1 = [7, 9, 6, 8, 5, 7, 10, 4, 6, 8, 5, 9, 6, 7, 4, 5, 8, 6, 7, 9, 5, 6]
# tiempos_maquina_2 = [8, 6, 7, 5, 9, 4, 6, 7, 8, 5, 4, 9, 7, 5, 8, 6, 7, 4, 5, 8, 6, 7]

# Caso Mediano 5 (25 Tareas)
# tiempos_maquina_1 = [6, 8, 5, 7, 4, 10, 6, 9, 7, 5, 8, 4, 9, 6, 10, 5, 7, 8, 6, 5, 9, 4, 8, 7, 5]
# tiempos_maquina_2 = [5, 7, 8, 6, 9, 5, 8, 7, 6, 10, 4, 5, 8, 6, 7, 9, 5, 6, 4, 8, 7, 5, 9, 6, 4]

# Case Extra Large 6 (40 Tasks)
# tiempos_maquina_1 = [15, 10, 8, 13, 7, 12, 9, 11, 6, 14, 5, 13, 10, 7, 16, 8, 9, 15, 11, 5, 12, 10, 14, 8, 6, 9, 15, 11, 5, 13, 8, 7, 10, 12, 14, 6, 11, 9, 15, 5]
# tiempos_maquina_2 = [10, 8, 12, 7, 15, 11, 6, 14, 10, 9, 13, 8, 5, 12, 10, 11, 9, 7, 15, 8, 6, 13, 9, 14, 10, 5, 11, 7, 12, 6, 14, 8, 13, 10, 9, 11, 6, 12, 7, 13]

# Run Genetic Algorithms
n_viajero(agente1, ciudades1)
print()
n_distribucion(tiempos_maquina_1, tiempos_maquina_2)
print()
n_reinas(8)
