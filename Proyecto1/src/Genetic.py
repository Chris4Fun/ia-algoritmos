import random
from collections import OrderedDict

# Import necessary modules for each problem
import Distribucion as dist
import NReinas as reinas
import Viajero as viajero

# Genetic Algorithm for N-Queens Problem
def genetic_n_reinas(n, num_generations=50, tamano_poblacion=10, probabilidad_mutacion=0.1):
    poblacion = [random.sample(range(n), n) for _ in range(tamano_poblacion)]
    
    for _ in range(num_generations):
        padre1, padre2 = seleccion(poblacion, problem='n_reinas', n=n)
        hijo = cruzamiento_reinas(padre1, padre2)
        mutacion_reinas(hijo, probabilidad_mutacion)
        reemplazar_hijo(hijo, poblacion, problem='n_reinas', n=n)
    
    mejor_solucion = obtener_mejor(poblacion, problem='n_reinas', n=n)
    conflictos = reinas.conflictos(mejor_solucion)
    
    print("\nSolución final para N-Reinas con algoritmo genético:")
    reinas.imprimir_tablero(mejor_solucion)
    print(f"Conflictos: {conflictos}")
    return mejor_solucion

# Genetic Algorithm for the Traveling Salesperson Problem
def genetic_viajero(agente, ciudades, num_generations=2, tamano_poblacion=10, probabilidad_mutacion=0.1):
    mejor_entregas = viajero.evaluar_ruta(agente, ciudades)
    print(f"Entregas iniciales: {mejor_entregas}")
    # Initialize population with actual 'Ciudad' objects, not indices
    poblacion = [random.sample(ciudades, len(ciudades)) for _ in range(tamano_poblacion)]

    for _ in range(num_generations):
        padre1, padre2 = seleccion(poblacion, problem='viajero', agente=agente)
        hijo = cruzamiento_viajero(padre1, padre2)
        mutacion_viajero(hijo, ciudades, probabilidad_mutacion)
        reemplazar_hijo(hijo, poblacion, problem='viajero', agente=agente)
    
    mejor_solucion = obtener_mejor(poblacion, problem='viajero', agente=agente)
    mejor_entregas = viajero.evaluar_ruta(agente, mejor_solucion)  # Evaluate using the agent and route
    
    print("\nSolución final para Viajero con algoritmo genético:")
    return mejor_solucion, mejor_entregas


# Genetic Algorithm for the Flow Shop Scheduling Problem
def genetic_distribucion(tiempos_maquina_1, tiempos_maquina_2, num_generations=2, tamano_poblacion=10, probabilidad_mutacion=0.1):
    num_tareas = len(tiempos_maquina_1)
    poblacion = [random.sample(range(num_tareas), num_tareas) for _ in range(tamano_poblacion)]
    
    for _ in range(num_generations):
        padre1, padre2 = seleccion(poblacion, problem='distribucion', tiempos_maquina_1=tiempos_maquina_1, tiempos_maquina_2=tiempos_maquina_2)
        hijo = cruzamiento_distribucion(padre1, padre2)
        mutacion_distribucion(hijo, probabilidad_mutacion)
        reemplazar_hijo(hijo, poblacion, problem='distribucion', tiempos_maquina_1=tiempos_maquina_1, tiempos_maquina_2=tiempos_maquina_2)
    
    mejor_solucion = obtener_mejor(poblacion, problem='distribucion', tiempos_maquina_1=tiempos_maquina_1, tiempos_maquina_2=tiempos_maquina_2)
    mejor_tiempo = dist.calcular_tiempos(mejor_solucion, tiempos_maquina_1, tiempos_maquina_2)
    
    print("\nSolución final para Distribución con algoritmo genético:")
    dist.imprimir(mejor_solucion, tiempos_maquina_1, tiempos_maquina_2)
    print(f"Makespan: {mejor_tiempo}")
    return mejor_solucion

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

def calcular_razon_n_reinas(individuo, **kwargs):
    n = kwargs.get('n')
    max_conflictos = n * (n - 1) / 2  # Máximo número de conflictos posibles
    conflictos = reinas.conflictos(individuo)
    fitness = max_conflictos - conflictos  # Queremos minimizar conflictos
    return fitness

def calcular_razon_distribucion(individuo, **kwargs):
    tiempos_maquina_1 = kwargs.get('tiempos_maquina_1')
    tiempos_maquina_2 = kwargs.get('tiempos_maquina_2')
    makespan = dist.calcular_tiempos(individuo, tiempos_maquina_1, tiempos_maquina_2)
    max_time = sum(tiempos_maquina_1) + sum(tiempos_maquina_2)
    fitness = max_time - makespan  # Queremos minimizar el makespan
    return fitness

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

# Cruzamiento y mutación para N-Reinas
def cruzamiento_reinas(padre1, padre2):
    punto_corte = random.randint(1, len(padre1) - 2)
    hijo = padre1[:punto_corte] + padre2[punto_corte:]
    # Resolver duplicados
    hijo = list(OrderedDict.fromkeys(hijo))
    faltantes = [i for i in range(len(padre1)) if i not in hijo]
    hijo.extend(faltantes)
    return hijo

def mutacion_reinas(individuo, probabilidad_mutacion):
    if random.random() <= probabilidad_mutacion:
        # Swap two random indices in the individual (solution)
        i, j = random.sample(range(len(individuo)), 2)
        individuo[i], individuo[j] = individuo[j], individuo[i]

# Cruzamiento y mutación para Viajero (Travelling Salesperson Problem)
def cruzamiento_viajero(padre1, padre2):
    # Crossover for 'Ciudad' objects
    punto_corte = random.randint(1, len(padre1) - 2)
    hijo = padre1[:punto_corte] + padre2[punto_corte:]
    
    # Remove duplicates while preserving the order
    hijo = list(OrderedDict.fromkeys(hijo))
    
    # Add missing cities to complete the route
    faltantes = [ciudad for ciudad in padre1 if ciudad not in hijo]
    hijo.extend(faltantes)
    return hijo

def mutacion_viajero(individuo, ciudades, probabilidad_mutacion):
    if random.random() <= probabilidad_mutacion:
        # Mutation involves swapping two random cities in the route (not numbers)
        i, j = random.sample(range(len(individuo)), 2)
        individuo[i], individuo[j] = individuo[j], individuo[i]

# Cruzamiento y mutación para Distribución (Flow Shop Scheduling)
def cruzamiento_distribucion(padre1, padre2):
    # Crossover for task assignment (still uses indices for tasks)
    punto_corte = random.randint(1, len(padre1) - 2)
    hijo = padre1[:punto_corte] + padre2[punto_corte:]
    
    # Remove duplicates while preserving the order
    hijo = list(OrderedDict.fromkeys(hijo))
    
    # Add missing tasks to complete the schedule
    faltantes = [tarea for tarea in padre1 if tarea not in hijo]
    hijo.extend(faltantes)
    return hijo

def mutacion_distribucion(individuo, probabilidad_mutacion):
    if random.random() <= probabilidad_mutacion:
        # Mutation for task assignment, swap two random tasks
        i, j = random.sample(range(len(individuo)), 2)
        individuo[i], individuo[j] = individuo[j], individuo[i]

# Example usage of the Genetic Algorithm for each problem

def n_reinas(n):
    genetic_n_reinas(n)

def n_distribucion(tiempos_maquina_1, tiempos_maquina_2):
    genetic_distribucion(tiempos_maquina_1, tiempos_maquina_2)

def n_viajero(agente, ciudades):
    mejor_ruta, mejor_entregas = genetic_viajero(agente, ciudades)
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
#n_distribucion(tiempos_maquina_1, tiempos_maquina_2)
#n_reinas(8)
