m=[1,4,5,3,2]
i=m.sort()
print("return of sort funvtion", i) # Sort function returns none

# Break, Continue and pass
i=10
while (i):
    if i%2==0:
        print("%d vale is Even Number"%(i))
        i=i-1
        continue # full iteration will be read, even condition is met.
    else:
         if i<=3:
             print("We do not count less than or equal to 3")
             break
             print("this line will never be printed under Break")
         else:
             pass
             print("this line will never be printed under pass")
             print("%d value is odd number"%(i))
             i=i-1




