import numpy as np
y  = np.array([[140, 155, 159, 179, 192, 200, 212, 215]]).T
x1 = np.array([[ 60,  62,  67,  70,  71,  72,  75,  78]]).T
x2 = np.array([[ 22,  25,  24,  20,  15,  14,  14,  11]]).T
ones = np.ones((8,1))
x = np.concatenate((ones, x1, x2), axis=1)
b = np.linalg.inv(x.T @ x) @ (x.T @ y)
for _ in [f'b{i}: {coeff[0]:.2f}\n' for (i, coeff) in enumerate(b)]: print(_)