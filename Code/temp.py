import numpy as np


a = np.random.rand(3, 4)
print(a)
print(a.mean(axis=1, keepdims=True))
b = a - a.mean(axis=1, keepdims=True)
print(b)

