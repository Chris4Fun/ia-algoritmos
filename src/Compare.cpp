#include "Compare.hpp"

Compare::Compare(const std::vector<int> objective_n) {
  this->objective = objective_n;
}
int Compare::similarityDegree(const std::vector<int>& board) {
  // Revisa cuántos elementos coinciden entre el tablero actual y el objetivo:
  int degree = 0;
  for (int i = 0; i < board.size(); i++) {
      if (board.at(i) == this->objective.at(i)) {
          degree++;
      }
  }
  return degree;
}

bool Compare::operator()(const std::vector<int>& vector1,
  const std::vector<int>& vector2) {
  return this->similarityDegree(vector1) < this->similarityDegree(vector2);
}