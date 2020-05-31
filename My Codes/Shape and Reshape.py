import numpy

ar = numpy.array([1,2,3,4,5,6,7,8])
print(ar.ndim, ar.shape)

##### using shape
ar.shape = (2,4) ### (x,y) m here x == column and y == rows
print(ar)

#### Using Reshape
ar = numpy.array([1,2,3,4,5,6,7,8])
ar = numpy.reshape(ar, (4,2))

print(ar)


ar = numpy.array(input().strip().split()[:9], int)
print(numpy.reshape(ar, (3,3)))
