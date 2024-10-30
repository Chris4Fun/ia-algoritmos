import random
import math
import time
import NReinas as reinas

class NQueensSimulatedAnnealing:

  def __init__(self, temperature_i: float, minTemperature_i: float,
      coolingRate_i: float, maxIterations_i: int, numberOfQueens_i: int):
    
    self.temperature = temperature_i
    self.minTemperature = minTemperature_i
    self.coolingRate = coolingRate_i
    self.maxIterations = maxIterations_i
    self.numberOfQueens = numberOfQueens_i
    # Board list: index represents column and value represents row
    # Queens are placed in a diagonal line: [0][0], [1][1], and so on...
    self.board = list(range(self.numberOfQueens))
    self.solutionIteration = -1
    random.shuffle(self.board)
    print("Tablero inicial:")
    reinas.imprimir_tablero(self.board)

  # Counts number of conflicts between queens in current solution:
  def calculateConflicts(self, board):
    conflicts = 0
    # Evaluates each queen pair:
    for i in range(self.numberOfQueens):
      for j in range(i + 1, self.numberOfQueens):
        # Checks conflict: same row OR diagonal colision:
        row = board[i] == board[j]
        mainDiagonal = (board[i] - board[j]) == (i - j)
        secondaryDiagonal = (board[i] + i) == (board[j] + j)
        if row or mainDiagonal or secondaryDiagonal:
          conflicts += 1
    return conflicts

  def createInitialSolution(self):
    random.shuffle(self.board)
    return self.board.copy() # returns a copy to keep array intact

  def createNewSolution(self, currentSolution: list):
    newSolution = currentSolution.copy()
    # Selects a random queen and puts her in a random row:
    col = random.randrange(0, self.numberOfQueens)
    row = random.randrange(0, self.numberOfQueens)
    newSolution[col] = row

    return newSolution

  def begin(self):
    currentSolution = self.createInitialSolution()
    currentConflicts = self.calculateConflicts(currentSolution)
    iterations = 0

    start_time = time.time()
    while self.temperature > self.minTemperature and iterations < self.maxIterations:
      newSolution = self.createNewSolution(currentSolution)
      newConflicts = self.calculateConflicts(newSolution)
      # Calculates conflict difference:
      difference = newConflicts - currentConflicts
      betterSolution = difference < 0
      # Accepts solution if it has less conflicts or by using probability:
      if betterSolution or random.random() < math.exp(-difference / self.temperature):
        currentSolution = newSolution
        currentConflicts = newConflicts

      # If solution is found:
      if currentConflicts == 0:
        self.solutionIteration = iterations

      # Update temperature:
      self.temperature = self.temperature * self.coolingRate
      iterations += 1

    end_time = time.time()
    self.printSolution(currentSolution, currentConflicts, iterations, end_time - start_time)
    return currentSolution

  def printSolution(self, solution: list, conflicts: int, iterations: int, exec_time: float):
    print(f"Solución encontrada en {self.solutionIteration} iteraciones con {conflicts} conflictos restantes.")
    print(f"Tiempo de ejecución: {exec_time:.4f} segundos")
    print("Tablero final:")
    reinas.imprimir_tablero(solution)

def run(numberOfQueens, temperature, minTemperature, coolingRate, maxIterations):
  sa = NQueensSimulatedAnnealing(temperature_i=temperature, minTemperature_i=minTemperature,
                          coolingRate_i=coolingRate, maxIterations_i=maxIterations, numberOfQueens_i=numberOfQueens)
  sa.begin()
  pass
