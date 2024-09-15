#include <vector>

class Compare {
 public:
  std::vector<int> objective;

  Compare(std::vector<int> objective_n);
  
  int similarityDegree(const std::vector<int>& board);
  bool operator()(const std::vector<int>& vector1,
    const std::vector<int>& vector2);
};