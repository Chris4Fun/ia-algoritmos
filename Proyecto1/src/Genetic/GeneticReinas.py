import random
from collections import OrderedDict

import NReinas as reinas

# Genetic Algorithm for N-Queens Problem
def genetic_n_reinas(n, num_generations=50, population_size=10, mutation_prob=0.1):
    poblacion = [random.sample(range(n), n) for _ in range(population_size)]
    
    for _ in range(num_generations):
        padre1, padre2 = seleccion(poblacion, n)
        hijo = cruzamiento_reinas(padre1, padre2)
        mutacion_reinas(hijo, mutation_prob)
        reemplazar_hijo(hijo, poblacion, n)
    
    mejor_solucion = obtener_mejor(poblacion, n)
    conflictos = reinas.conflictos(mejor_solucion)
    
    return mejor_solucion,  conflictos

# Operadores para Reinas

def seleccion(poblacion, n):
    poblacion_ordenada = sorted(poblacion, key=lambda ind: calcular_razon_n_reinas(ind, n), reverse=True)
    return poblacion_ordenada[0], poblacion_ordenada[1]

def cruzamiento_reinas(padre1, padre2):
    punto_corte = random.randint(1, len(padre1) - 2)
    hijo = padre1[:punto_corte] + padre2[punto_corte:]
    hijo = list(OrderedDict.fromkeys(hijo))
    faltantes = [i for i in range(len(padre1)) if i not in hijo]
    hijo.extend(faltantes)
    return hijo

def mutacion_reinas(individuo, mutation_prob):
    if random.random() <= mutation_prob:
        i, j = random.sample(range(len(individuo)), 2)
        individuo[i], individuo[j] = individuo[j], individuo[i]

def reemplazar_hijo(hijo, poblacion, n):
    peor_individuo = poblacion[0]
    peor_valor = calcular_razon_n_reinas(peor_individuo, n)
    
    peor_indice = 0
    for i, individuo in enumerate(poblacion):
        valor_actual = calcular_razon_n_reinas(individuo, n)
        if valor_actual < peor_valor:
            peor_valor = valor_actual
            peor_individuo = individuo
            peor_indice = i

    poblacion[peor_indice] = hijo

# Funciones auxiliares

def calcular_razon_n_reinas(individuo, n):
    max_conflictos = n * (n - 1) / 2  # Máximo número de conflictos posibles
    conflictos = reinas.conflictos(individuo)
    fitness = max_conflictos - conflictos  # Queremos minimizar conflictos
    return fitness

def obtener_mejor(poblacion, n):
    mejor_individuo = poblacion[0]
    mejor_valor = calcular_razon_n_reinas(mejor_individuo, n)
    
    for individuo in poblacion:
        valor_actual = calcular_razon_n_reinas(individuo, n)
        if valor_actual > mejor_valor:
            mejor_valor = valor_actual
            mejor_individuo = individuo

    return mejor_individuo