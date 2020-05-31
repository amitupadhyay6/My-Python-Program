
cd=[]
i=0
while i<10:
    cd.append(int(input(f"enter the {i+1} number = ")))
    i+=1
print(cd)

j=1
j=n=len(cd)-1
while n!=0:
    x=cd[n]
    while j!=0:
        if cd[j-1]==x:
            cd.pop(j-1)
            n=n-1
        j-=1
    n=n-1
    j=n
print("dup removed list is ", cd)
#########################################



