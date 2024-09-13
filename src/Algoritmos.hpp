#ifndef ALGORITMOS_HPP
#define ALGORITMOS_HPP

#include <bits/stdc++.h>
using namespace std;

class Algoritmos {
 private:
  double timeElapsed = 0;
  vector<int> tablero = {3, 2, 1, 4, 8, 6, 7, 5, 0};
  vector<vector<int>> posiblesMovimientos(const vector<int>& current);

 public:
  Algoritmos();
  ~Algoritmos();

  void shuffle();

  // Algoritmos
  void anchoPrimero();
  void greedy();
  void solucionadorIDS();
  void IDSHeuristica();

};

#endif //ALGORITMOS_HPP