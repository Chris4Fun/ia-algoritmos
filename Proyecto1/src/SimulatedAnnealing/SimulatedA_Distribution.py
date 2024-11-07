import random
import math
import time
import Distribucion as dist

class DistributionSimulatedAnnealing:
    def __init__(self, temperature_i: float, minTemperature_i: float, coolingRate_i: float, 
                 maxIterations_i: int, machineOneTimes_i: list, machineTwoTimes_i: list):
        self.temperature = temperature_i
        self.minTemperature = minTemperature_i
        self.coolingRate = coolingRate_i
        self.maxIterations = maxIterations_i
        self.machineOneTimes = machineOneTimes_i
        self.machineTwoTimes = machineTwoTimes_i

    def generateNewDistribution(self, currentDist: list):
        return dist.cambios_asignacion(currentDist)
        
    def begin(self):
        currentDist = dist.primera_asignacion(self.machineOneTimes, self.machineTwoTimes)
        currentTime = dist.calcular_tiempos(currentDist, self.machineOneTimes, self.machineTwoTimes)
        iterations = 0

        start_time = time.perf_counter()
        while self.temperature > self.minTemperature and iterations < self.maxIterations:
            newDist = random.choice(self.generateNewDistribution(currentDist))
            newTime = dist.calcular_tiempos(newDist, self.machineOneTimes, self.machineTwoTimes)
            # Calculates time difference:
            timeDifference = newTime - currentTime
            # Accepts solution if it has more value or by using probability:
            if timeDifference < 0 or random.random() < math.exp(-timeDifference / self.temperature):
                currentDist = newDist
                currentTime = newTime

            # Update temperature:    
            self.temperature *= self.coolingRate
            iterations += 1

        end_time = time.perf_counter()
        print("\nDistribución Final:")
        dist.imprimir(currentDist, self.machineOneTimes, self.machineTwoTimes)
        print("Tiempo de ejecución: {:.8f} s".format(end_time - start_time))

def run(machineOneTimes, machineTwoTimes, temperature, minTemperature, coolingRate, maxIterations):
    
    sa = DistributionSimulatedAnnealing(
        temperature_i=10000.0, minTemperature_i=0.001,
        coolingRate_i=0.95, maxIterations_i=10000,
        machineOneTimes_i=machineOneTimes,
        machineTwoTimes_i=machineTwoTimes
    )    
    sa.begin()

