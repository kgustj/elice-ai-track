import numpy as np


def AND(x1, x2):
    x = np.array([x1, x2])
    y = np.array([0.5, 0.5])
    b = -0.7  # theta θ

    temp = np.sum(x * y) + b
    if temp <= 0:
        return 0
    else:
        return 1


# x1w1 + x2w2 + b = 0
# 0.5x + 0.5y - 0.7 = 0
# 5x + 5y - 7 = 0
# 5y = -5x + 7
# y = -x + 7/5

print(AND(0, 0))
print(AND(0, 1))
print(AND(1, 0))
print(AND(1, 1))
