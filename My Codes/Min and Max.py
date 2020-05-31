
# 1st min then Max on the poutput

import numpy

n,m = input().strip().split()[:2]
n = int(n)
m = int(m)
ar = []
for i in range(n):
    ar.append(list(map(int,input().strip().split()[:m])))
Aarray = numpy.array(ar)
min = numpy.min(Aarray, axis=1)
print(numpy.max(min))

# print(np.max(np.min(np.array([input().split() for _ in range(int(input().split()[0]))],int),axis=1)))
