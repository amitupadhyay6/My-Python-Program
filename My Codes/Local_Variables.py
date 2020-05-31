# When you declare variables inside a function definition, they are not related in any way to
# other variables with the same names used outside the function - i.e. variable names are
# local to the function. This is called the scope of the variable. All variables have the scope of
# the block they are declared in starting from the point of definition of the name.

x=5

def func(x):
    print("X is ", x)
    x=2
    print("\nX value has been changed in the function and new value of X is ", x)

func(x)
print("\nValue of x variable out of the function scope is ", x)
