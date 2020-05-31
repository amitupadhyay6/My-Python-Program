
import numpy

Aar = numpy.array((input().strip().split()), dtype=int)
Bar = numpy.array((input().strip().split()), dtype=int)

print(numpy.inner(Aar,Bar))
print(numpy.outer(Aar,Bar))
