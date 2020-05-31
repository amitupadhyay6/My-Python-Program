from itertools import combinations_with_replacement

s, k = input().split()

s = list (s)
s.sort()

m = list((combinations_with_replacement(s,int(k))))
sK = ""
print(m)
for i in range(0,len(m)):
    for j in range(0, int(k)):
        sK = sK + m[i][j]
    print(sK)
    sK = ""

