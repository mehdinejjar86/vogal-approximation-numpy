import numpy as np
from vogel import vogel_approximation_method

if __name__ == "__main__":
  cost_matrix = np.array([[9, 5, 7, 6],
                        [6, 1, 2, 4],
                        [1, 6, 4, 9]], dtype=np.float64)
  supply = np.array([2400, 2800, 1900])
  demand = np.array([1900, 1500, 1800, 1900])

  result = vogel_approximation_method(cost_matrix, supply, demand)
  print(result)
