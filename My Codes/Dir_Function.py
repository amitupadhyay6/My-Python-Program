
''' The dir function
Built-in dir() function returns list of names defined by an object. If the object is a module,
this list includes functions, classes and variables, defined inside that module.
This function can accept arguments. If the argument is the name of the module, function
returns list of names from that specified module. If there is no argument, function returns list
of names from the current module.'''

# Use CMD for the output
import mymodule
import sys
import math

dir(mymodule)

a=5
b=10
dir()
dir(sys)
dir(math)
dir(str)

