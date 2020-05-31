# floor/Ceil - tool rounds to floor/Ceil input element-wise.
# rint -  The rint tool rounds to the nearest integer of input element-wise.


import numpy

numpy.set_printoptions(sign=' ')
Aarray = numpy.array((input().split()), dtype= float)
print(numpy.floor(Aarray))
print(numpy.ceil(Aarray))
print(numpy.rint(Aarray))
