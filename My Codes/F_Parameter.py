#A function can take parameters, which are values you supply to the function so that the function can do something utilising those values.
# These parameters are just like variables except that the values of these variables are defined when we call the function and are
# already assigned values when the function runs.

# Parameters are specified within the pair of parentheses in the function definition, separated by commas.
# When we call the function, we supply the values in the same way. Note the terminology used - the names given in the function
# definition are called parameters whereas the values you supply in the function call are called arguments.

def PMax(a, b):
    if a>b:
        print(a, " is bigger than ", b)
    elif a<b:
        print(b, " is bigger than", a)
    else:
        print(a, " is equal to ", b)

print("type two number and check which one is bigger\n")
y=int(input("Enter your 1st number "))
z=int(input("Enter your 2nd number "))

print("\nCalling Funstion\n")
# passing variables as arguments
PMax(y,z)
print("Parameter has been passed to function and result has been shown on the screen")

