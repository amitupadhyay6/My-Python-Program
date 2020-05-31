l = []
def lis(n):
    if n[0] == "insert":
        l.insert(int(n[1]),int(n[2]))
    elif n[0] == "print":
        print(l)
    elif n[0] == "remove":
        l.remove(int(n[1]))
    elif n[0] == "append":
        l.append(n[1])
    elif n[0] == "sort":
        l.sort()
    elif n[0] == "pop":
        l.pop(len(l)-1)
    elif n[0] == "reverse":
        l.reverse()


for i in range(int(input())):
    x = input().strip().split()[:3]
    lis(x)
