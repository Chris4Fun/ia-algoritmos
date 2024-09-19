#ifndef ALGORITMOS_HPP
#define ALGORITMOS_HPP

#include <bits/stdc++.h>
#include <algorithm>
#include <random>
#include <utility>

#include "Compare.hpp"

using namespace std;

class Algoritmos {
 private:
  // Contador de tiempo:
  double timeElapsed = 0;
  // Matriz/Tablero objetivo:
  const vector<int> objetivo = {1, 2, 3, 4, 5, 6, 7, 8, 0};
  // Tablero de juego:
  vector<int> tablero = {3, 2, 1, 4, 8, 6, 7, 5, 0};

  vector<vector<int>> posiblesMovimientos(const vector<int>&);

  int heuristicaManhattan(const vector<int>& movimientoActual);
  bool dls(vector<int>& estado, int limite);

 public:
  Algoritmos();
  ~Algoritmos();
  void shuffle();
  void printBoard();
  
  // Auxiliares
  int idsHeuristicaAuxiliar(std::vector<int> estadoActual, 
                             std::set<std::vector<int>> visitados,
                             int costo, int limite);

  // Algoritmos
  bool anchoPrimero();
  bool anchoPrimeroHeuristica();
  void ids();
  void IDSHeuristica();

};

#endif //ALGORITMOS_HPP
