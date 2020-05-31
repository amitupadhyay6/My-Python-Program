
# A NumPy array is a grid of values. They are similar to lists, except that every element of an array must be the same type.

import numpy

def arrays(arr):
    arr = numpy.array(arr, float)
    return arr[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
