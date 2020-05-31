
import Module1

for i in Module1.sys.path:
    print("The Python Path is : ", i)

'''# Module1 has been called and its variable has been used here, so 1st complier/interpreter has executed the imported
# mdole, latre this module

#Byte-compiled .pyc files
Importing a module is a relatively costly affair, so Python does some tricks to make it faster.
One way is to create byte-compiled files with the extension .pyc which is an intermediate
form that Python transforms the program into (remember the introduction section on how
Python works?). This .pyc file is useful when you import the module the next time from a
different program - it will be much faster since a portion of the processing required in
importing a module is already done. Also, these byte-compiled files are platformindependent.'''


