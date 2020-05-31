# If you want to assign a value to a name defined at the top level of the program (i.e. not inside
# any kind of scope such as functions or classes), then you have to tell Python that the name
# is not local, but it is global. We do this using the global statement. It is impossible to assign
# a value to a variable defined outside a function without the global statement.

x=5

def func():
    # using global keywork we can use the variable defined outside of the scope of the function
    global x
    print(x)
    x=2
    print(x)
func()
print("Value of X outside the function and it has been changed as it is defined in the function as global"
      "value of X has been updated in the function ", x)

# You can specify more than one global variable using the same global statement e.g. global x, y, z
