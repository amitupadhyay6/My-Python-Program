#we can not sort the dictionary using the old fashion using indexing, as dictionary does not support the indexing, it works on the key methods only.
#We can sort the output of key,value and item functon which returns the list and tuples.
d={3:"Eva",2:"Vibha",1:"Amit",5:"Mangal",4:"Shivam"}
print("Unsorted dictionay is ", d)
k=d.keys()
m=list(k) # converted the list funcion output in the list using list() function.
v=d.values()
z=list(v) # converted the list funcion output in the list using list() function.
n=len(d)-1
i=0
while i!=n:
    j=n
    while j!=0:
        if m[j]<m[j-1]:
            temp=m[j-1]
            m[j-1]=m[j]
            m[j]=temp
            ex=z[j-1]
            z[j-1]=z[j]
            z[j]=ex
            j=j-1
        else:
            j=j-1
    i=i+1
i=0
dict={}
while i!=n+1:
    dict[m[i]]=z[i]
    i=i+1
print("Sorted Dictionary is ", dict)




