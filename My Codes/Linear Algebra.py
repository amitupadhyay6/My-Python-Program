# linalg.det - The linalg.det tool computes the determinant of an array.
#print numpy.linalg.det([[1 , 2], [2, 1]])       #Output : -3.0

# linalg.eig - The linalg.eig computes the eigenvalues and right eigenvectors of a square array.
# vals, vecs = numpy.linalg.eig([[1 , 2], [2, 1]])
# print vals                                      #Output : [ 3. -1.]
# print vecs                                      #Output : [[ 0.70710678 -0.70710678]
                                                #          [ 0.70710678  0.70710678]]
# linalg.inv - The linalg.inv tool computes the (multiplicative) inverse of a matrix.
# print numpy.linalg.inv([[1 , 2], [2, 1]])       #Output : [[-0.33333333  0.66666667]
#                                                #          [ 0.66666667 -0.33333333]]
import numpy

numpy.set_printoptions(legacy="1.13")
n = int(input())

array2d = numpy.array([(input().strip().split()[:n]) for i in range(n)], dtype=float)

print(numpy.linalg.det(array2d))



