cd=[]
i=0
while i<5:
    cd.append(int(input("Enter 5 random number tpo find the sorted list, num = ")))
    i+=1
print(cd)

j=0
i=4
k=0
while j!=5:
    k=0
    while k!=i:
        if cd[k] > cd[k+1]:
            temp=cd[k+1]
            cd[k+1]=cd[k]
            cd[k]=temp
            k = k+1
        else:
            k=k+1
    j+=1
    i-=1
print(f"sorted list is {cd}")





