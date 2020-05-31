#not imutable
cd=(1,2,3)
print(cd.index(3))

# save items of tuple in variable
cd=(2,3,4)
x=cd[0]
y=cd[1]
z=cd[2]
print(x*y*z)

# unpacking can be used for list as well
x,y,z=cd
print(x*y*z)

cd=[2,5,4]
x,y,z=cd
print(x*y*z)

