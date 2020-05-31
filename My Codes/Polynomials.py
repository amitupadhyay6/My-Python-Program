
# Polynomials is combination of terms with "+" or "-" and terms are (number * variable) - example x2-2xb+b2 - number == coefficient of term
# nv = Monomials, nv +(-) nv = binomials, nv +(-) nv +(-) nv = Trinomials, rest are Polynomails. all can be called polynomials

import numpy

polyarray = numpy.array([float(x) for x in input().strip().split()])
print(polyarray)
print(numpy.polyval(polyarray, float(input())))
