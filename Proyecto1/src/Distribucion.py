# Funciones comunes para resolver el problema de distribucion de trabajo
import random

def primera_asignacion(tiempos_maquina_1, tiempos_maquina_2):
    return random.sample(range(5), 5)

def calcular_tiempos(asignacion_actual, tiempos_maquina_1, tiempos_maquina_2):
    final_tiempo_1 = 0
    final_tiempo_2 = 0

    for producto in asignacion_actual:
        # Desempaquetar la tupla de producto
        index = producto
        
        # Tiempo de finalización en máquina A
        final_tiempo_1 += tiempos_maquina_1[index]
        
        # Tiempo de finalización en máquina B
        final_tiempo_2 = max(final_tiempo_1, final_tiempo_2) + tiempos_maquina_2[index]
    
    return final_tiempo_2

def cambios_asignacion(asignacion_actual):
    vecinos = []
    for i in range(5):
        for j in range(i + 1, 5):
            # Intercambiar dos productos en la solución para generar un vecino
            nueva_asignacion = asignacion_actual[:]
            nueva_asignacion[i], nueva_asignacion[j] = nueva_asignacion[j], nueva_asignacion[i]
            vecinos.append(nueva_asignacion)
    return vecinos

def imprimir(asignacion, tiempos_maquina_1, tiempos_maquina_2):
    print("Producto | Máquina A (inicio, fin) | Máquina B (inicio, fin)")
    finish_time_A = 0
    finish_time_B = 0
    
    for index in asignacion:
        start_time_A = finish_time_A
        finish_time_A += tiempos_maquina_1[index]
        
        start_time_B = max(finish_time_A, finish_time_B)
        finish_time_B = start_time_B + tiempos_maquina_2[index]
        
        print(f"P{index + 1}       | ({start_time_A}, {finish_time_A})      | ({start_time_B}, {finish_time_B})")
    
    print(f"Hace span óptimo: {finish_time_B}")