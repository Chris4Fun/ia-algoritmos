import random
from collections import OrderedDict

import Viajero as viajero

# Genetic Algorithm for the Traveling Salesperson Problem
def genetic_viajero(agente, ciudades, num_generations=50, tamano_poblacion=10, mutation_prob=0.1):
   
    poblacion = [random.sample(ciudades, len(ciudades)) for _ in range(tamano_poblacion)]

    for _ in range(num_generations):
        padre1, padre2 = seleccion(poblacion, agente)
        hijo = cruzamiento_viajero(padre1, padre2)
        mutacion_viajero(hijo, ciudades, mutation_prob)
        reemplazar_hijo(hijo, poblacion, agente)
    
    mejor_solucion = obtener_mejor(poblacion, agente)
    mejor_entregas = viajero.evaluar_ruta(agente, mejor_solucion)
    
    return mejor_solucion, mejor_entregas

# Operadores para Viajero
def seleccion(poblacion, agente):
    # Selecciona los dos mejores individuos de la población
    poblacion_ordenada = sorted(poblacion, key=lambda ind: viajero.evaluar_ruta(agente, ind), reverse=True)
    return poblacion_ordenada[0], poblacion_ordenada[1]
    

def cruzamiento_viajero(padre1, padre2):
    punto_corte = random.randint(1, len(padre1) - 2)
    hijo = padre1[:punto_corte] + padre2[punto_corte:]
    
    hijo = list(OrderedDict.fromkeys(hijo))
    
    faltantes = [ciudad for ciudad in padre1 if ciudad not in hijo]
    hijo.extend(faltantes)
    return hijo

def mutacion_viajero(individuo, ciudades, mutation_prob):
    if random.random() <= mutation_prob:
        # Intercambia dos ciudades de manera aleatoria
        i, j = random.sample(range(len(individuo)), 2)
        individuo[i], individuo[j] = individuo[j], individuo[i]


# Funciones auxiliares

def obtener_mejor(poblacion, agente):
    mejor_individuo = poblacion[0]
    mejor_valor = viajero.evaluar_ruta(agente, mejor_individuo)
    
    for individuo in poblacion:
        valor_actual = viajero.evaluar_ruta(agente, individuo)
        if valor_actual > mejor_valor:
            mejor_valor = valor_actual
            mejor_individuo = individuo

    return mejor_individuo

def reemplazar_hijo(hijo, poblacion, agente):
    # Reemplaza el individuo con el menor valor en la población con el nuevo hijo
    peor_individuo = poblacion[0]
    peor_valor = viajero.evaluar_ruta(agente, peor_individuo)
    
    peor_indice = 0
    for i, individuo in enumerate(poblacion):
        valor_actual = viajero.evaluar_ruta(agente, individuo)

        if valor_actual < peor_valor:
            peor_valor = valor_actual
            peor_individuo = individuo
            peor_indice = i
    poblacion[peor_indice] = hijo

