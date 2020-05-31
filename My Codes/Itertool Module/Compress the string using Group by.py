from itertools import groupby

str = input()
#numbers = [1, 1, 1, 3, 3, 2, 2, 2, 1, 1]
l = []
for (key, group) in groupby(str):
    #print(list(group))
    l.append([list(group), key])

for i in range(0,len(l)):
    l[i][0] = len(l[i][0])
    l[i] = (l[i][0], int(l[i][1]))

print(*l)
