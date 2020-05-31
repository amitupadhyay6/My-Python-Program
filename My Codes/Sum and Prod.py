
import numpy

ar = numpy.array([ [1,2], [7,10]])
print(ar.sum())
print(numpy.sum(ar, axis=0))
print(numpy.sum(ar, axis=1))
print(numpy.sum(ar, axis=None))
print(numpy.sum(ar))
print("\n")
print(ar.prod())
print(numpy.prod(ar, axis=0))
print(numpy.prod(ar, axis=1))
print(numpy.prod(ar, axis=None))
print(numpy.prod(ar))
