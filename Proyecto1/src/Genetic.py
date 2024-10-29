
# Import necessary modules for each problem
import Distribucion as dist
import NReinas as reinas
import Viajero as viajero

# Import each genetic algorithmm
from Genetic.GeneticDist import *
from Genetic.GeneticReinas import *
from Genetic.GeneticViaj import *

# Functions used to call each algorithm separately

def n_reinas(n):
    mejor_solucion, conflictos = genetic_n_reinas(n)
    print("\nSolución final para N-Reinas con algoritmo genético:")
    reinas.imprimir_tablero(mejor_solucion)
    print(f"Conflictos: {conflictos}")

def n_distribucion(tiempos_maquina_1, tiempos_maquina_2):
    mejor_solucion, mejor_tiempo = genetic_distribucion(tiempos_maquina_1, tiempos_maquina_2)
    print("\nSolución final para Distribución con algoritmo genético:")
    dist.imprimir(mejor_solucion, tiempos_maquina_1, tiempos_maquina_2)
    print(f"Makespan: {mejor_tiempo}")

def n_viajero(agente, ciudades):
    mejor_entregas = viajero.evaluar_ruta(agente, ciudades)
    print(f"Entregas iniciales: {mejor_entregas}")
    mejor_ruta, mejor_entregas = genetic_viajero(agente, ciudades)
    print("\nSolución final para Viajero con algoritmo genético:")
    viajero.imprimir(mejor_ruta, mejor_entregas)

# Example initialization and usage

ciudades = [
    viajero.Ciudad("A", "recolectar", suministra=10),
    viajero.Ciudad("B", "entregar", demanda=5),
    viajero.Ciudad("C", "recolectar", suministra=7),
    viajero.Ciudad("D", "entregar", demanda=8),
    viajero.Ciudad("E", "entregar", demanda=6),
]

agente = viajero.Viajero(capacidad=15)

tiempos_maquina_1 = [2, 6, 3, 4, 2]
tiempos_maquina_2 = [7, 2, 5, 3, 6]

# Run Genetic Algorithms
n_viajero(agente, ciudades)
print()
n_distribucion(tiempos_maquina_1, tiempos_maquina_2)
print()
n_reinas(8)
