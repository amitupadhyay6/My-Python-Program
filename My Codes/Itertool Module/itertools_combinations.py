from itertools import combinations

st, k = input().split()
st = list(st)
st.sort()
for f in range(1, int(k)+1):
    print(f)
    m = list((combinations(st,f)))
    s = ""
    for i in range(0,len(m)):
        for j in range(0,f):
            s = s + m[i][j]
        print(s)
        s = ""






