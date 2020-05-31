# If you have some functions with many parameters and you want to specify only some of them, then you can give values for
# such parameters by naming them - this is called keyword arguments - we use the name (keyword) instead of the position
# (which we have been using all along) to specify the arguments to the function. There are two advantages - one,
# using the function is easier since we do not need to worry about the order of the arguments. Two, we can give values
# to only those parameters to which we want to, provided that the other parameters have default argument values.

def fun(a, b=5, c=10):
    print("Value of a is ", a," Value of b is ", b," Value of c is ", c)
print("Function defined as func(a,b=5,c=10)\n")
fun(a=5,c=20)
print("\ncalling function 2nd time")
fun(c=100, b=15, a=13)
print("\ncalling function 3rd time")
fun(10)
