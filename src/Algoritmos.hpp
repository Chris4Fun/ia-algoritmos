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
  const vector<int> objetivo = {0, 1, 2, 3, 4, 5, 6, 7, 8};
  // Tablero de juego:
  vector<int> tablero = {1, 4, 2, 3, 5, 8, 0, 6, 7};

  vector<vector<int>> posiblesMovimientos(const vector<int>&);

  int heuristica(const vector<int>&);
  bool dls(vector<int>&, int);
  bool dlsHeuristica(vector<int>&, int, int);  
 public:
  Algoritmos();
  ~Algoritmos();
  void shuffle();
  void asignarTablero(const vector<int>&);
  void imprimirTablero();

  // Algoritmos
  bool anchoPrimero();
  bool anchoPrimeroHeuristica();
  void ids();
  void IDSHeuristica();

};

#endif //ALGORITMOS_HPP
