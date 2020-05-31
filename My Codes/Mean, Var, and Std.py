import numpy

numpy.set_printoptions(sign=' ')
numpy.set_printoptions(legacy='1.13')
n,m = map(int, input().strip().split()[:2])
ar = numpy.array(([input().strip().split()[:m] for i in range(n)]), int)
print(ar)

# Mean at Axis = 1
print(numpy.mean(ar,dtype= float, axis=1))

# Variance at Axix =0
print(numpy.var(ar, dtype=float, axis=0))

# Standard Deviation at Axis = none or don't mention axis
print(numpy.std(ar, dtype=float, axis=None))
