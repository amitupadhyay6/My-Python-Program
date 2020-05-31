
import numpy

n = int(input())
Aar = numpy.array(([input().strip().split()[:n] for i in range(n)]), dtype=int)
Bar = numpy.array(([input().strip().split()[:n] for i in range(n)]), dtype=int)

print(numpy.dot(Aar,Bar))
