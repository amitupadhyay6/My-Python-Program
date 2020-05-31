# k is number of list, m is modulus s= (f(x1)+.......+f(xk)%m
#k, m = input().strip().split()[:2]
#int(k); int(m)
k = 7; m =867
dict = {}
for i in range(1, k+1):
    x = list(map(int, input().strip().split()))
    dict[i] = x[1:x[0]+1]
print(dict)
tempnumber = 0


def fsquare(kmax):
    return kmax*kmax


for key in dict:
    tempnumber = tempnumber + fsquare(max(dict[key]))
    print(max(dict[key]), key)
smax = tempnumber % m
print(smax)




