
#Concatenate - Two or more arrays can be concatenated together using the concatenate function with a tuple of the arrays to be joined:
import numpy

########## axis = 1 is no of rows and axis =0 no of column

n,m, p = input().strip().split()[:3]
ar = []
for i in range(int(n)):
    ar.append(list(map(int,input().strip().split()[:int(p)])))
Aarray = numpy.array(ar)
ar = []
for i in range(int(m)):
    ar.append(list(map(int, input().strip().split()[:int(p)])))
Barray = numpy.array(ar)

concatenate_array = numpy.concatenate((Aarray,Barray), axis=0)
print(concatenate_array)

