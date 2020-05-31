x=[]
y=input("Enter random numbers !! ", )
i=len(y)
k=i-1
print("total number typed are {} and numbers are {} ".format(i,y))
l=0
while l<i:
    x.append(y[l])
    l=l+1
print("the list is - ", x)
while i!=0:
    j=k
    while j!=0:
        if x[j] <= x[j-1]:
            a=x[j-1]
            x[j-1]=x[j]
            x[j]=a
            j=j-1
        else:
            j=j-1
    i=i-1
print("Sorted numbers are : ", x)
# Used the empty list and used append to add user input and used the list to sort the number
'''There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.'''
m=[1,4,5,3,2]
i=m.sort()
print("return of sort funvtion", i) # Sort function returns none
