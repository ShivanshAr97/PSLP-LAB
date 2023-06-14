import numpy as np
from scipy.optimize import linear_sum_assignment

cost = np.array([[4, 2, 1], [3, 5, 2], [1, 3, 5]])

row_ind, col_ind = linear_sum_assignment(cost)

print("Optimal value:", cost[row_ind, col_ind].sum())
print("Optimal assignments:", list(zip(row_ind, col_ind)))