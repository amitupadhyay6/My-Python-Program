
#str = input()
str = "1222311"
str = list(str)
print(str)
i = 0
l = []
while i < len(str):
    temp = str[i]
    count = 1
    j = i+1
    while j < len(str):
        if j == len(str)-1:
             if str[j] == temp:
                count = count + 1
                i += 1
                break
             else:
                 break
        else:
            if str[j] == temp and str[j+1] == temp:
                count = count + 2
                j += 2
                i += 2
                break
            else:
                break
    l.append((count,int(temp)))
    i += 1

print(*l)

