import numpy as np
print("Test if two arrays are element-wise equal within a tolerance:")

print(np.allclose([10,7], [[16,17],[5,4]],1,0))

# print(np.allclose([1e10,1e-8], [1.00001e10,1e-9]))
# print(np.allclose([1e10,1e-8], [1.0001e10,1e-9]))
# print(np.allclose([1.0, np.nan], [1.0, np.nan]))
# print(np.allclose([1.0, np.nan], [1.0, np.nan], equal_nan=True))

x = np.array([[3.14159265, -0.1], [-0.1, 0.1]])

z1 = np.array([[[3.14159265, -0.1], [-0.1, 0.1]],
              [[3.14159265, -0.1], [-0.1, 0.1]]])


print(np.allclose(x, z1))