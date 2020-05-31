# 1st add then product on the output
import numpy

n,m = input().strip().split()[:2]
n = int(n)
m = int(m)
ar = []
for i in range(n):
    ar.append(list(map(int,input().strip().split()[:m])))
Aarray = numpy.array(ar)
sumarray = numpy.sum(Aarray, axis = 0)
print(numpy.product(sumarray))



