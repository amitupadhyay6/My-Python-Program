from itertools import permutations

#s, n = input().split()
s = "HACKA"; n =2
m = list((permutations(s,int(n))))
m.sort()
i = 0
s = ""
l = []
while i < len(m):
    for j in range(0, int(n)):
        s = s + m[i][j]
    if s not in l:
        l.append(s)
        print(s)
        s = ""
        i += 1
    else:
        s = ""
        i +=1

















