
n, m = map(int,input().strip().split()[:2])
ar = list(map(int,input().strip().split()[:n]))
a = list(map(int,input().strip().split()[:m]))
b = list(map(int,input().strip().split()[:m]))
nl = []
nl.append(ar[0])
count = 1

for item in ar:
    if item not in nl:
        nl.append(item)
        if item in a:
            count += 1
        elif item in b:
            count -= 1

print(count)




