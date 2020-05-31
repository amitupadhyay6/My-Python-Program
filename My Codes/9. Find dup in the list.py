cd=[]
i=0
while i<10:
    cd.append(int(input("Enter 10 random number to find dup in the list, num = ")))
    i+=1
print(cd)
j=0
l=0
k= len(cd) - 1

for i in cd:
    m=i
    j=l
    while j!=k:
        if m==cd[j + 1]:
            print(f" {m} is duplicate number")
            j+=1
        else:
            j+=1
    l+=1




