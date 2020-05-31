dic ={}
for i in range(int(input())):
     a,b,c,d = (input().split())
     float(b), float(c), float(d)
     dic[a] = [b,c,d]


def find_avg(n):
    x = dic[n]
    y = (float(x[0])+float(x[1])+float(x[2]))/3
    return "{:.2f}".format(y)


print(find_avg(input()))


