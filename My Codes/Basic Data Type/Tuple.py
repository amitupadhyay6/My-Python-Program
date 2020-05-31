
def rtup():
    i = int(input())
    d = input().strip().split()[:i]
    for i in range(len(d)):
        d[i] = int(d[i])
    return d


t = tuple(rtup())
print(hash(t))
