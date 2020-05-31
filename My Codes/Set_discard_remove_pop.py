n = int(input())
setlist = set(map(int, input().split()[:n]))

def setf(n):
    if n[0] == "pop":
        if len(setlist) != 0:
            setlist.pop()
    elif n[0] == "remove":
        if int(n[1]) in setlist:
            setlist.remove(int(n[1]))
    elif n[0] == "discard":
        setlist.discard(int(n[1]))


for i in range(int(input())):
    x = input().strip().split()[:2]
    setf(x)
z = 0
for item in setlist:
        z = z + int(item)
print(z)
