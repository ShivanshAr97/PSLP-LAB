import numpy as np
from scipy.optimize import linprog

c = [-2, -3, -4]
A = [[1, 2, 3], [2, 5, 3]]
b = [30, 45]
x0_bounds=(0, None)
x1_bounds=(0, None)
x2_bounds=(0, None)

res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds, x2_bounds], method='simplex')

print("Optimal value:", -res.fun)
print("Optimal solution:", res.x)