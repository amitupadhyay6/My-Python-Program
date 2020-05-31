# zeros - The zeros tool returns a new array with a given shape and type filled with 's.
# print numpy.zeros((1,2), dtype = numpy.int) #Type changes to int


# Ones - The ones tool returns a new array with a given shape and type filled with 's.
# print numpy.ones((1,2), dtype = numpy.int) #Type changes to int

import numpy

nums = tuple(map(int, input().split()))
print (numpy.zeros(nums, dtype = numpy.int))
print (numpy.ones(nums, dtype = numpy.int))


