import random
import math
import time
import Viajero as viajero
from Viajero import *

class TSMSimulatedAnnealing:

  def __init__(self, temperature_i: float, minTemperature_i: float,
               coolingRate_i: float, maxIterations_i: int, salesmanCapacity_i: int,
               cities_i: list[Ciudad]):
    
    self.temperature = temperature_i
    self.minTemperature = minTemperature_i
    self.coolingRate = coolingRate_i
    self.maxIterations = maxIterations_i
    self.salesman = Viajero(salesmanCapacity_i)
    self.cities = cities_i

# ----------------------------------------------------------------------------------
  def createInitialSolution(self):
    return viajero.evaluar_ruta(self.salesman, self.cities)

  def createNewSolution(self, currentRoute: list[Ciudad]):
    all_possible_routes = cambios_ruta(currentRoute)
    return random.choice(all_possible_routes)

  def begin(self):
      currentSolution = self.cities
      currentSolutionValue = self.createInitialSolution()
      iterations = 0

      start_time = time.perf_counter()
      while self.temperature > self.minTemperature and iterations < self.maxIterations:
        newSolution = self.createNewSolution(currentSolution)
        newSolutionValue = viajero.evaluar_ruta(self.salesman, newSolution)
        # Calculates value difference:
        difference = newSolutionValue - currentSolutionValue
        betterSolution = difference > 0
        # Accepts solution if it has more value or by using probability:
        if betterSolution or random.random() < math.exp(difference / self.temperature):
          currentSolution = newSolution
          currentSolutionValue = newSolutionValue

        # Update temperature:
        self.temperature *= self.coolingRate
        iterations += 1

      end_time = time.perf_counter()
      self.printSolution(currentSolution, currentSolutionValue, end_time - start_time)
      return currentSolution

  def printSolution(self, solution: list, currentSolutionValue: int, exec_time: float):
      print(f"Tiempo de ejecución: {exec_time:.8f} segundos")
      print("Ruta definida:")
      viajero.imprimir(solution, currentSolutionValue)

def run(salesmanCapacity, cities, temperature, minTemperature, coolingRate, maxIterations):
  sa = TSMSimulatedAnnealing(
      temperature_i=temperature, minTemperature_i=minTemperature,
      coolingRate_i=coolingRate, maxIterations_i=maxIterations,
      salesmanCapacity_i=salesmanCapacity, cities_i=cities
  )
  sa.begin()
  pass
