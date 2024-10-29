
# Import necessary modules for each problem
import Distribucion as dist
import NReinas as reinas
import Viajero as viajero

# Import each genetic algorithmm
from Genetic.GeneticDist import *
from Genetic.GeneticReinas import *
from Genetic.GeneticViaj import *


# Funciones auxiliares adaptadas para cada problema

def obtener_mejor(poblacion, problem, **kwargs):
    # Encuentra el individuo con el mejor valor en la población
    mejor_individuo = poblacion[0]
    if problem == 'n_reinas':
        mejor_valor = calcular_razon_n_reinas(mejor_individuo, **kwargs)
    elif problem == 'viajero':
        mejor_valor = viajero.evaluar_ruta(agente, mejor_individuo)
    elif problem == 'distribucion':
        mejor_valor = calcular_razon_distribucion(mejor_individuo, **kwargs)
    
    for individuo in poblacion:
        if problem == 'n_reinas':
            valor_actual = calcular_razon_n_reinas(individuo, **kwargs)
        elif problem == 'viajero':
            valor_actual = viajero.evaluar_ruta(agente, individuo)
        elif problem == 'distribucion':
            valor_actual = calcular_razon_distribucion(individuo, **kwargs)

        if valor_actual > mejor_valor:
            mejor_valor = valor_actual
            mejor_individuo = individuo
    return mejor_individuo

def reemplazar_hijo(hijo, poblacion, problem, **kwargs):
    # Reemplaza el individuo con el menor valor en la población con el nuevo hijo
    peor_individuo = poblacion[0]
    if problem == 'n_reinas':
        peor_valor = calcular_razon_n_reinas(peor_individuo, **kwargs)
    elif problem == 'viajero':
        peor_valor = viajero.evaluar_ruta(agente, peor_individuo)
    elif problem == 'distribucion':
        peor_valor = calcular_razon_distribucion(peor_individuo, **kwargs)
    
    peor_indice = 0
    for i, individuo in enumerate(poblacion):
        if problem == 'n_reinas':
            valor_actual = calcular_razon_n_reinas(individuo, **kwargs)
        elif problem == 'viajero':
            valor_actual = viajero.evaluar_ruta(agente, individuo)
        elif problem == 'distribucion':
            valor_actual = calcular_razon_distribucion(individuo, **kwargs)

        if valor_actual < peor_valor:
            peor_valor = valor_actual
            peor_individuo = individuo
            peor_indice = i
    poblacion[peor_indice] = hijo

# Separate functions to calculate the fitness (razón) for each problem





# Operadores del algoritmo genético adaptados para cada problema

def seleccion(poblacion, problem, **kwargs):
    # Selecciona los dos mejores individuos de la población
    if problem == 'n_reinas':
        poblacion_ordenada = sorted(poblacion, key=lambda ind: calcular_razon_n_reinas(ind, **kwargs), reverse=True)
    elif problem == 'viajero':
        poblacion_ordenada = sorted(poblacion, key=lambda ind: viajero.evaluar_ruta(agente, ind), reverse=True)
    elif problem == 'distribucion':
        poblacion_ordenada = sorted(poblacion, key=lambda ind: calcular_razon_distribucion(ind, **kwargs), reverse=True)
    
    return poblacion_ordenada[0], poblacion_ordenada[1]




# Example usage of the Genetic Algorithm for each problem

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
