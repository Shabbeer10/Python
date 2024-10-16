# import numpy as np
# from numpy import pi

# a = np.array([2,3,4])
# print(a.dtype)

# b = np.array([1.2, 3.5, 5.1])
# print(b.dtype)

# This line of code `b = np.array([(1.5, 2, 3),(4, 5, 6)])` is creating a NumPy array `b` with shape
# (2, 3) containing the specified values. The array `b` is a 2-dimensional array with 2 rows and 3
# columns. Each row is specified as a tuple of values within the square brackets.
# b = np.array([(1.5, 2, 3),(4, 5, 6)])
# print(b)

# The line `c = np.array([[1, 2],[3, 4]], dtype=complex)` is creating a NumPy array `c` with a
# specified data type of complex numbers. The array `c` is a 2-dimensional array with 2 rows and 2
# columns. The values in the array are integers, but by specifying `dtype=complex`, the integers are
# converted to complex numbers.
# c = np.array([[1, 2],[3, 4]], dtype = complex)
# print(c)

# `zeros = np.zeros((3, 4))` is creating a NumPy array `zeros` with a shape of (3, 4) filled with
# zeros. This means that the array `zeros` is a 2-dimensional array with 3 rows and 4 columns, and all
# the elements in the array are set to zero.
# zeros = np.zeros((3, 4))
# print(zeros)

# `ones = np.ones((2,3,4), dtype = np.int16)` is creating a NumPy array named `ones` with a shape of
# (2, 3, 4). This means that the array `ones` is a 3-dimensional array with 2 matrices, each matrix
# having 3 rows and 4 columns.
# ones = np.ones((2,3,4), dtype = np.int16)
# print(ones)

# `empty = np.empty((2,3))` is creating a NumPy array named `empty` with a shape of (2, 3). This means
# that the array `empty` is a 2-dimensional array with 2 rows and 3 columns.
# empty = np.empty((2,3))
# print(empty)

# The line `range = np.arange(10, 30, 5)` is using NumPy's `arange` function to create an array that
# starts at 10, increments by 5, and stops before reaching 30.
# range = np.arange(10, 30, 5)
# print(range)

# `linspace = np.linspace(0, 2, 9)` is creating a NumPy array `linspace` that contains 9 evenly spaced
# numbers over the interval [0, 2].
# linspace = np.linspace(0, 2 * pi, 100)
# `linspace2 = np.linspace(0, 2, 9)` is creating a NumPy array `linspace2` that contains 9 evenly
# spaced numbers over the interval [0, 2]. In this case, the function `linspace` generates an array of
# 9 elements starting from 0, ending at 2, and evenly spaced between those two values.
# linspace2 = np.linspace(0, 2, 9)
# print(linspace2)

# aa = np.arange(6)
# print(aa)

# bb = np.arange(12).reshape(4, 3)
# print(bb)

# cc = np.arange(24).reshape(2, 3, 4)
# print(cc)

# The code `print(np.arange(10000).reshape(100, 100))` is creating a NumPy array with 10,000 elements
# using `np.arange(10000)` which generates an array of numbers from 0 to 9999. Then, it reshapes this
# 1D array into a 2D array with a shape of (100, 100) using the `reshape(100, 100)` method. Finally,
# it prints this 2D array where each row contains 100 elements.
# print(np.arange(10000).reshape(100, 100))

# A = np.array([[1, 1],
#              [0, 1]])
# B = np.array([[2, 0],
#              [3, 4]])

# print(A * B)
# print(A @ B)
# print(A.dot(B))

# rg = np.random.default_rng(1)
# a =np.ones((2, 3), dtype =int)
# b = rg.random((2, 3))
# a *= 3
# print(a)
# b += a
# print(b)
