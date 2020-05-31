
# You have seen how you can reuse code in your program by defining functions once. What if you wanted to reuse a number of functions
# in other programs that you write? As you might have guessed, the answer is modules. There are various methods of writing modules,
# but the simplest way is to create a file with a .py extension that contains functions and variables.
# Another method is to write the modules in the native language in which the Python interpreter itself was written.

#A module can be imported by another program to make use of its functionality. This is how we can use the Python standard library as well.
# First, we will see how to use the standard library modules.

import sys
# Imported inbuild module Sys
print("Command Line Arg : ", sys.argv, "\n")
print(" The command line arguments are ")
for i in sys.argv:
    print("Arguments :",i)
print("\n\n the PYTHONPATH is ", sys.path, "\n")
list(sys.argv)

# Use comand line argument to see the arguments

#Note that the current directory is the directory from which the program is launched. Run import os; print(os.getcwd())
# to find out the current directory of your program.
