# identity - The identity tool returns an identity array. An identity array is a square matrix with all the main diagonal elements as  and the rest as .
# The default type of elements is float.
# numpy.identity(n, dtype=None)[source]¶

#eye - The eye tool returns a 2-D array with 's as the diagonal and 's elsewhere. The diagonal can be main, upper or lower depending on the optional parameter .
#A positive  is for the upper diagonal, a negative  is for the lower, and a   (default) is for the main diagonal.
# numpy.eye(N, M=None, k=0, dtype=<class 'float'>, order='C')[source]

#N : int Number of rows in the output.
#M : int, optional - Number of columns in the output. If None, defaults to N.
#k : int, optional - Index of the diagonal: 0 (the default) refers to the main diagonal, a positive value refers to an upper diagonal, and a negative value to a lower diagonal.
#dtype : data-type, optional - Data-type of the returned array

import numpy

print(numpy.identity(3, dtype=int))
print(numpy.eye(3,4, k =1, dtype=numpy.int))

n, m = input().strip().split()[:2] # n = rows, m = column
n = int(n)
m = int(m)
if n == m:
    x = str(numpy.identity(n)).replace('1.', ' 1. ')
    print((numpy.identity(n)))
else:
    x = str(numpy.eye(n,m, k =0)).replace('1.', ' 1. ')
    print(x)
