from itertools import product


a = list(map(int,input().strip().split()))
b = list(map(int,input().strip().split()))
c = product(a,b)
for item in c:
    print(item, end=" ")
