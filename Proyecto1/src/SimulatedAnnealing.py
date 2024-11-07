import Distribucion as dist
import NReinas as reinas
import Viajero as viajero
import SimulatedAnnealing.SimulatedA_NQueens as nQueens
import SimulatedAnnealing.SimulatedA_TSM as TSM
import SimulatedAnnealing.SimulatedA_Distribution as dist


temperature = 100000
minTemperature = 0.01
coolingRate = 0.99
iterations = 10000

ciudades = [
    viajero.Ciudad("A", "recolectar", suministra = 10),
    viajero.Ciudad("B", "entregar", demanda = 5),
    viajero.Ciudad("C", "recolectar", suministra = 7),
    viajero.Ciudad("D", "entregar", demanda = 8),
    viajero.Ciudad("E", "entregar", demanda = 6),
]
# Create an agent with a max capacity of 15
agente = viajero.Viajero(capacidad = 15)


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


# tiempos_maquina_1 = [2, 6, 3, 4, 2]
# tiempos_maquina_2 = [7, 2, 5, 3, 6]

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

# tiempos_maquina_1 = [15, 10, 8, 13, 7, 12, 9, 11, 6, 14, 5, 13, 10, 7, 16, 8, 9, 15, 11, 5, 12, 10, 14, 8, 6, 9, 15, 11, 5, 13, 8, 7, 10, 12, 14, 6, 11, 9, 15, 5]
# tiempos_maquina_2 = [10, 8, 12, 7, 15, 11, 6, 14, 10, 9, 13, 8, 5, 12, 10, 11, 9, 7, 15, 8, 6, 13, 9, 14, 10, 5, 11, 7, 12, 6, 14, 8, 13, 10, 9, 11, 6, 12, 7, 13]


print("---------------------------------------------------------")
print("Agente Viajero")
print("---------------------------------------------------------")
TSM.run(agente1, ciudades1, temperature = temperature, minTemperature = minTemperature, coolingRate=coolingRate, maxIterations = iterations)
print("---------------------------------------------------------")
print("Distribución")
print("---------------------------------------------------------")
dist.run(tiempos_maquina_1, tiempos_maquina_2, temperature = temperature, minTemperature = minTemperature, coolingRate=coolingRate, maxIterations = iterations)
print("---------------------------------------------------------")
print("N Reinas")
print("---------------------------------------------------------")
nQueens.run(8, temperature = temperature, minTemperature = minTemperature, coolingRate=coolingRate, maxIterations = iterations)
print("---------------------------------------------------------")