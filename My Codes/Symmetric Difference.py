sortedlist = []
m = int(input())
mset = input().strip().split()[:m]
n = int(input())
nset = input().strip().split()[:n]
i =0
for item in mset:
    if item not in nset:
        if item not in sortedlist:
            sortedlist.append(item)
print("after 1st iter", sortedlist)

for item in nset:
    if item not in mset:
        if item not in sortedlist:
                sortedlist.append(item)
print("after second", sortedlist)

sl = []
for item in sortedlist:
    sl.append(int(item))
sl.sort()
for item in sl:
    print(item)

