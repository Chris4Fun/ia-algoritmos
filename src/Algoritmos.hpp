#ifndef ALGORITMOS_HPP
#define ALGORITMOS_HPP

class Algoritmos {
 private:
  double timeElapsed = 0;

 public:
  Algoritmos();
  ~Algoritmos();

// Algoritmos

  void anchoPrimero();
  void greedy();
  void solucionadorIDS();
  void IDSHeuristica();

};

#endif //ALGORITMOS_HPP