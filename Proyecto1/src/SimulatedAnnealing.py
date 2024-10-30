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

tiempos_maquina_1 = [2, 6, 3, 4, 2]
tiempos_maquina_2 = [7, 2, 5, 3, 6]

print("---------------------------------------------------------")
print("Agente Viajero")
print("---------------------------------------------------------")
TSM.run(agente, ciudades, temperature = temperature, minTemperature = minTemperature, coolingRate=coolingRate, maxIterations = iterations)
print("---------------------------------------------------------")
print("Distribución")
print("---------------------------------------------------------")
dist.run(tiempos_maquina_1, tiempos_maquina_2, temperature = temperature, minTemperature = minTemperature, coolingRate=coolingRate, maxIterations = iterations)
print("---------------------------------------------------------")
print("N Reinas")
print("---------------------------------------------------------")
nQueens.run(8, temperature = temperature, minTemperature = minTemperature, coolingRate=coolingRate, maxIterations = iterations)
print("---------------------------------------------------------")