cd=[1,2,3,4,2,3,2,3,2,2]
temp=[]
for i in cd:
    if i not in temp:
        temp.append(i)
print(temp)
