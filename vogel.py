import numpy as np

def calculate_difference(cost_matrix):
    flag = 0
    row_length = cost_matrix.shape[0]
    column_length = cost_matrix.shape[1]

    row_difference = np.zeros(row_length, dtype=np.float64)
    column_difference = np.zeros(column_length, dtype=np.float64)
    
    for i in range(len(row_difference)):
        indexes = cost_matrix[i].argsort()[:2]
        if cost_matrix[i][indexes[0]] == np.inf or cost_matrix[i][indexes[1]] == np.inf:
            row_difference[i] = -1
        else:
            row_difference[i] = abs(cost_matrix[i][indexes[0]] - cost_matrix[i][indexes[1]])

    cost_matrixT = cost_matrix.T
    
    for i in range(len(column_difference)):
        indexes = cost_matrixT[i].argsort()[:2]
        if cost_matrixT[i][indexes[0]] == np.inf or cost_matrixT[i][indexes[1]] == np.inf:
            column_difference[i] = -1
        else:
            column_difference[i] = abs(cost_matrixT[i][indexes[0]] - cost_matrixT[i][indexes[1]])
    
    return row_difference, column_difference

def vogel_approximation_method(cost_matrix, supply, demand):
    result = np.zeros(shape=cost_matrix.shape, dtype=np.int32)
    total_demand = demand.sum()
    
    while total_demand > result.sum():
    
        r, c = calculate_difference(cost_matrix=cost_matrix)
        if c.max() >= r.max() and (c[0] != -1 or r[0] != -1):
            column_index = c.argmax()
            
            position_indexes = cost_matrix[:,column_index].argsort()
            for position_index in position_indexes:
                s = supply[position_index]
                d = demand[column_index]
                if s >= d:
                    demand[column_index] -= d
                    supply[position_index] -= d
                    result[position_index, column_index] = d
                    for j in range(len(r)):
                        cost_matrix[j, column_index] = np.inf
                    break
                else:
                    demand[column_index] -= s
                    supply[position_index] -= s
                    result[position_index, column_index] = s
        
        else:
            row_index = r.argmax()
            
            position_indexes = cost_matrix[row_index].argsort()
            for position_index in position_indexes:
                s = supply[row_index]
                d = demand[position_index]
                if s >= d:
                    demand[position_index] -= d
                    supply[row_index] -= d
                    result[row_index, position_index] = d
                    for j in range(len(c)):
                        cost_matrix[row_index, j] = np.inf
                    break
                else:
                    demand[position_index] -= s
                    supply[row_index] -= s
                    result[row_index, position_index] = s

    return result