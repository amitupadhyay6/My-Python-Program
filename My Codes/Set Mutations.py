n = int(input())
alist = list(map(int, input().strip().split()[:n]))
alist = set(alist)

for i in range(int(input())):
    comand, setsize = input().strip().split()[:2]
    setsize = int(setsize)
    if comand == "intersection_update":
        blist = list(map(int, input().strip().split()[:setsize]))
        alist.intersection_update(blist)
    elif comand == "difference_update":
        blist = list(map(int, input().strip().split()[:setsize]))
        alist.difference_update(blist)
    elif comand == "symmetric_difference_update":
        blist = list(map(int, input().strip().split()[:setsize]))
        alist.symmetric_difference_update(blist)
    elif comand == "update":
        blist = list(map(int, input().strip().split()[:setsize]))
        alist.update(blist)
alist = list(alist)
x = 0
for i in range(len(alist)):
    x = x + int(alist[i])
print(x)

