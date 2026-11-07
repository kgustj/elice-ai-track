import numpy as np

A = np.array([[6, 2], [9, 0]])
B = np.linalg.inv(A)

print(np.round(B, 3))
print(np.dot(A, B))
