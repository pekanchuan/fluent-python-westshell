import numpy as np

a = np.arange(12)

print(a.shape)

a.shape = 3, 4
print(a)
print(a[:, 1])
print(a.transpose())
