#https://www.hackerrank.com/challenges/nested-list/problem
mar = []
for i in range(int(input())):
    ar = []
    ar.append(input())
    ar.append(float(input()))
    mar.append(ar)
n = len(mar)
i = 0
while i < n:
    j = 0
    while j < n-1:
        if mar[j][1] > mar[j+1][1]:
            x = mar[j+1]
            mar[j+1] = mar[j]
            mar[j] = x
            j += 1
        else:
            j += 1
    i += 1
i=0
cd=[]
while i < n-1:
    if mar[i][1] == mar[i+1][1]:
        i += 1
    else:
        te = mar[i+1][1]
        j=i
        while j < n-1:
            if mar[j+1][1] == te:
                cd.append(mar[j+1][0])
                j += 1
            else:
                j += 1
        break
cd.sort()
for item in cd:
    print(item)
