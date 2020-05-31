import numpy

n,m = input().strip().split()[:2]
n = int(n)
m = int(m)
ar = []
for i in range(n):
    ar.append(list(map(int,input().strip().split()[:m])))
Aarray = numpy.array(ar)
ar = []
for i in range(n):
    ar.append(list(map(int,input().strip().split()[:m])))
Barray = numpy.array(ar)

print(Aarray + Barray)
print(Aarray - Barray)
print(Aarray * Barray)
print(Aarray // Barray)
print(Aarray % Barray)
print(Aarray ** Barray)




