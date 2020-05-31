n, m = input().split()
n = int (n)
m = int(m)
d="-"
p=".|."
l=(m-3)//2
u = (m - 7) // 2
w="WELCOME"
x=1
# 9 27
i = 0
for i in range(n):
    if i == (n)//2:
        print(u*d+w+u*d)
        i += 1
    else:
        if i < (n+1)//2:
            print(l*d+p*x+l*d)
            l = l - 3
            x = x + 2
            i += 1
        else:
            l = l + 3
            x = x - 2
            print(l*d+p*x+l*d)
            i += 1








