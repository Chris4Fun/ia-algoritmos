#ifndef ALGORITMOS_HPP
#define ALGORITMOS_HPP

#include <bits/stdc++.h>
using namespace std;

class Algoritmos {
 private:
  double timeElapsed = 0;
  vector<int> tablero = {3, 2, 1, 4, 8, 6, 7, 5, 0};
  vector<vector<int>> posiblesMovimientos(const vector<int>&);

 public:
  Algoritmos();
  ~Algoritmos();

  void shuffle();

  // Auxiliares
  int iterativeDeepeningDfs(vector<int> estado, set<vector<int>> &visitados, int depth);

  // Algoritmos
  bool anchoPrimero();
  void greedy();
  void solucionadorIDS();
  void IDSHeuristica();

};

#endif //ALGORITMOS_HPP