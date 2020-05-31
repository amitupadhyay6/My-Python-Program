# The return statement is used to return from a function i.e. break out of the function. We can optionally return
# a value from the function as well.

def max(a,b):
    if a>b:
        return a
    elif a==b:
        return "A is equal to B"
    else:
        return b

print("Below value is returned from called function, please give your input\n")
print(   max(   int(input("enter your 1st number ")), int(input("enter your 2nd number "))     )     )

print("\n Try Again\n")
print(   max(   int(input("enter your 1st number ")), int(input("enter your 2nd number "))     )     )

print("\n Try Again\n")
print(   max(   int(input("enter your 1st number ")), int(input("enter your 2nd number "))     )     )

