import numpy as np
X = np.array([1, 7, 13, 105,"hello world "])
print("Original array:")
print(X)
print("Size of the memory occupied by the said array:")
print(X.dtype)
print("%d bytes" % (X.size * X.itemsize))