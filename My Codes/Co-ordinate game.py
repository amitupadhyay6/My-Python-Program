x = int(input())
y = int(input())
z = int(input())
n = int(input())
l=[]
i=0
while i>=0 and i<=x:
    t=[]
    #t.append(i)
    j=0
    while j>=0 and j<=y:
        k=0
        while k>=0 and k<=z:
            t=[i,j,k]
            l.append(t)
            k+=1
        j+=1
    i+=1
m=0 ### below code is to remove entry where x+y+z == n
while m<len(l):
    if (l[m][0]+l[m][1]+l[m][2])==n:
        l.pop(m)
    else:
        m+=1
print(l)


