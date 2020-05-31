happiness = 0
n, m = input().strip().split()[:2]
n = int(n)
m = int(m)
array = list(map(int,input().strip().split()[:n]))
aset = set(map(int, input().strip().split()[:m]))
bset = set(map(int,input().strip().split()[:m]))
intersection = aset.intersection(bset)
aset = aset.difference(intersection)
bset = bset.difference(intersection)

for i in range(0, n):
    if array[i] in aset:
        happiness = happiness + 1
    elif array[i] in bset:
        happiness = happiness - 1
print(happiness)


