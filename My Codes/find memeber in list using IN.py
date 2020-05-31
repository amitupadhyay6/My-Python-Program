
ab=["1","a",2,3,4,5,5,6]
c="a" in ab # it returns true
d=8 in ab # it returns False
print("If c=1 then \"a\" is found", c, "If d=0, means 8 is not found din the list ", d)

# Learning loops

for i in ab: # Use ":" this to inform compiler that you are using loop and line ends here
    if i==6:
        print("last element is found", i)
    else:
        print("Still Searching for the last item")



