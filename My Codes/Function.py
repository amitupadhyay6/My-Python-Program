
# Functions are defined using the def keyword. After this keyword comes an identifier name
# for the function, followed by a pair of parentheses which may enclose some names of
# variables, and by the final colon that ends the line. Next follows the block of statements that
# are part of this function.

def say_hello():
    # Block belonging to the function
    print("Hello World")
# End of function

print("Calling Function")
say_hello()
print("\nCalling function again")
say_hello()

def say_hello():
    print("Two function with same name")
print("\nCalling updated function")
say_hello()



