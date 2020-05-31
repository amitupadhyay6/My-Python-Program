#Raw String
print(r' \a\n\x99 ')

a=[0,1,2,3]
b=["i am lonely", "lean on"]
d=[a,b] #d=[[1,2,3,4],["a","b",'c',"d"]] can be written in this way
print(d)
print(d[1])
print(d[0][2])
print(d[0][0:2]) #Slicing
print(len(d))
#d=d[0]+"Number"  #You can not add String with list, you need to add list only
e=d[0]+["Amit"]
print(e)
print(d*2)
print(len(d))

#List is not imutable like string
m=[0,1,2,3,4,9]
m[4:5]={4,5,6,7,8} # you can add item in between the list items
print(m)
del m[5:9]
print("Deleted the item added to the list", m)
