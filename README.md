# Vogel's Approximation Method (VAM) for Transportation Problems

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Table of Contents
- [Vogel's Approximation Method (VAM) for Transportation Problems](#vogels-approximation-method-vam-for-transportation-problems)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [About Vogel's Approximation Method (VAM)](#about-vogels-approximation-method-vam)
  - [Project Structure](#project-structure)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Running the Example](#running-the-example)
    - [Using with Custom Data](#using-with-custom-data)
  - [Example Data](#example-data)
  - [Contributing](#contributing)
  - [License](#license)

## Introduction

This repository provides a straightforward Python implementation of **Vogel's Approximation Method (VAM)**, a widely used heuristic for finding an initial basic feasible solution to transportation problems. VAM is known for producing solutions that are often very close to the optimal solution, making it an excellent starting point for further optimization using methods like the Stepping Stone or MODI method.

## About Vogel's Approximation Method (VAM)

The transportation problem is a special type of linear programming problem that deals with the distribution of a commodity from various sources (origins) to various destinations. The objective is to minimize the total cost of transportation while satisfying supply and demand constraints.

VAM works on the principle of minimizing "penalty" or "opportunity costs." For each row and column in the cost matrix, it calculates a penalty cost, which is the difference between the two lowest costs. The method then prioritizes making allocations in the row or column with the highest penalty, choosing the cell with the minimum cost within that row/column. This greedy approach, informed by opportunity cost, tends to yield a more efficient initial solution compared to other methods like the Northwest Corner Rule or the Least Cost Method.

## Project Structure

```

.
├── main.py        \# Main script demonstrating VAM usage with an example.
└── vogel.py       \# Core implementation of the Vogel's Approximation Method.

````

## Installation

To get started with this project, simply clone the repository and install the necessary dependencies.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/vogel-approximation-method.git](https://github.com/yourusername/vogel-approximation-method.git)
    cd vogel-approximation-method
    ```
    (Remember to replace `yourusername/vogel-approximation-method` with your actual repository path)

2.  **Install dependencies:**
    This project only requires `numpy`.
    ```bash
    pip install numpy
    ```

## Usage

### Running the Example

To see Vogel's Approximation Method in action with a predefined example, simply run the `main.py` script:

```bash
python main.py
````

This will print the step-by-step cost matrix and allocation matrix transformations, finally outputting the initial basic feasible solution (the allocation matrix).

### Using with Custom Data

You can easily integrate the `vogel_approximation_method` function into your own Python projects.

1.  **Import the function:**

    ```python
    from vogel import vogel_approximation_method
    ```

2.  **Define your `cost_matrix`, `supply`, and `demand` arrays:**

      * `cost_matrix`: A 2D NumPy array (float64 recommended) where `cost_matrix[i, j]` is the cost of transporting one unit from source `i` to destination `j`.
      * `supply`: A 1D NumPy array representing the available supply at each source.
      * `demand`: A 1D NumPy array representing the required demand at each destination.

    **Important:** Ensure that the total supply is equal to or greater than the total demand for the problem to be solvable as implemented. If `supply.sum() < demand.sum()`, the function will return `-1`. For unbalanced problems (where demand \> supply), a dummy source with zero cost is typically added to balance it, which is not handled automatically by this implementation.

3.  **Call the method:**

    ```python
    # Example:
    my_cost_matrix = np.array([[C11, C12], [C21, C22]], dtype=np.float64)
    my_supply = np.array([S1, S2])
    my_demand = np.array([D1, D2])

    allocation_result = vogel_approximation_method(my_cost_matrix, my_supply, my_demand)
    print(allocation_result)
    ```

## Example Data

The `main.py` uses the following example for demonstration:

**Cost Matrix (`cost_matrix`):**

```
[[9, 5, 7, 6],
 [6, 1, 2, 4],
 [1, 6, 4, 9]]
```

**Supply (`supply`):**

```
[2400, 2800, 1900]
```

**Demand (`demand`):**

```
[1900, 1500, 1800, 1900]
```

## Contributing

Contributions are welcome\! If you have suggestions for improvements, bug fixes, or new features (e.g., handling unbalanced problems, visualization), please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.
