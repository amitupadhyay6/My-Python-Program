# For some functions, you may want to make some parameters optional and use default values in case the user does not want to provide values
# for them. This is done with the help of default argument values. You can specify default argument values for parameters by
# appending to the parameter name in the function definition the assignment operator ( = ) followed by the default value.
# Note that the default argument value should be a constant.

def func(m, t=1):
    print(m*t)

print("Passing only one variable hello to the function\n")
func("hello")
print("\nPassing both the variables hello and 5 to the function\n")
func("Hello",5)

