import random
from collections import OrderedDict

import Distribucion as dist

# Genetic Algorithm for the Flow Shop Scheduling Problem
def genetic_distribucion(time_1, time_2, num_generations=50, tamano_poblacion=10, mutation_prob=0.1):
    num_tareas = len(time_1)

    poblacion = [random.sample(range(num_tareas), num_tareas) for _ in range(tamano_poblacion)]
    
    for _ in range(num_generations):
        padre1, padre2 = seleccion(poblacion, time_1, time_2)
        hijo = cruzamiento_distribucion(padre1, padre2)
        mutacion_distribucion(hijo, mutation_prob)
        reemplazar_hijo(hijo, poblacion, time_1, time_2)
    
    mejor_solucion = obtener_mejor(poblacion, time_1, time_2)
    mejor_tiempo = dist.calcular_tiempos(mejor_solucion, time_1, time_2)
    
    return mejor_solucion, mejor_tiempo

# Operadores para Distribucion

def seleccion(poblacion, time_1, time_2):
    poblacion_ordenada = sorted(poblacion, key=lambda ind: calcular_razon_distribucion(ind, time_1, time_2), reverse=True)
    return poblacion_ordenada[0], poblacion_ordenada[1]

def cruzamiento_distribucion(padre1, padre2):
    punto_corte = random.randint(1, len(padre1) - 2)
    hijo = padre1[:punto_corte] + padre2[punto_corte:]
    
    hijo = list(OrderedDict.fromkeys(hijo))
    
    faltantes = [tarea for tarea in padre1 if tarea not in hijo]
    hijo.extend(faltantes)
    return hijo

def mutacion_distribucion(individuo, mutation_prob):
    if random.random() <= mutation_prob:
        i, j = random.sample(range(len(individuo)), 2)
        individuo[i], individuo[j] = individuo[j], individuo[i]

#Funciones auxiliares

def reemplazar_hijo(hijo, poblacion, time_1, time_2):
    peor_individuo = poblacion[0]
    peor_valor = calcular_razon_distribucion(peor_individuo, time_1, time_2)
    
    peor_indice = 0
    for i, individuo in enumerate(poblacion):
        valor_actual = calcular_razon_distribucion(individuo, time_1, time_2)

        if valor_actual < peor_valor:
            peor_valor = valor_actual
            peor_individuo = individuo
            peor_indice = i
    poblacion[peor_indice] = hijo

def obtener_mejor(poblacion, time_1, time_2):
    mejor_individuo = poblacion[0]
    mejor_valor = calcular_razon_distribucion(mejor_individuo, time_1, time_2)
    
    for individuo in poblacion:
        valor_actual = calcular_razon_distribucion(individuo, time_1, time_2)
        if valor_actual > mejor_valor:
            mejor_valor = valor_actual
            mejor_individuo = individuo

    return mejor_individuo

def calcular_razon_distribucion(individuo, time_1, time_2):
    makespan = dist.calcular_tiempos(individuo, time_1, time_2)
    max_time = sum(time_1) + sum(time_2)
    print(max_time)
    fitness = max_time - sum(makespan)
    return fitness