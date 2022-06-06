import numpy as np


def OR(x1, x2):
    x = np.array([x1, x2])
    y = np.array([0.5, 0.5])
    b = -0.2  # theta θ
    temp = np.sum(x * y) + b
    print(temp)
    if temp <= 0:
        return 0
    else:
        return 1


# def OR(x1, x2):
#     w1, w2, b = 1, 1, 0.5
#     return 0 if x1 * w1 + x2 * w2 <= b else 1

# x1w1 + x2w2 + b = 0
# 0.5x + 0.5y - 0.2 = 0
# 5x + 5y - 2 = 0
# 5y = -5x + 2
# y = -x + 2/5

print(OR(0, 0))  # 0.5 * 0 + 0.5 * 0 + -0.2 = -0.2 < 0 => 0
print(OR(0, 1))  # 0.5 * 0 + 0.5 * 1 + -0.2 = +0.3 > 0 => 1
print(OR(1, 0))  # 0.5 * 1 + 0.5 * 0 + -0.2 = +0.3 > 0 => 1
print(OR(1, 1))  # 0.5 * 1 + 0.5 * 1 + -0.2 = +0.8 > 0 => 1
