# this progream is to find the duplicate number in the list

list= ["1","2","3","1","1","9","0","1"]
print(list)
n=len(list)
m=n
print(n, m)
x=0
while n!=0:
    j=0
    while j!=m:
       z=list[x]
       if z==list[j]:
           print(z, " is repeated at ", j+1 )
           j=j+1
       else:
           j=j+1
    x=x+1
    n=n-1







