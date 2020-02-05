import numpy as np
import tabulate as tabulate

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ndmin=2)

print("Array is of type", type(arr))

print("Array is of dimension", arr.ndim)

print("Array is of shape", arr.shape)

print("Array is of size", arr.size)

# print(arr)

table = tabulate.tabulate(arr, tablefmt="fancy_grid")

print(table)

new = arr > 5

table2 = tabulate.tabulate(new, tablefmt="fancy_grid")

print(table2)

