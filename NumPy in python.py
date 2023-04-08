# NumPy in python
# numPy is a general purpose array processing package
# it provides a powerful N dimensional array object
# sofisticated functions, linear algebra , fourier transform , and random number capabilities

import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
print("array is if type:", type(arr))

print ("number of dimensions:", arr.ndim)

print("shape of array:", arr.shape)

print("size of array:", arr.size)

print("array stores elements of type:", arr.dtype)