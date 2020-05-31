# The from..import statement

''' If you want to directly import the argv variable into your program (to avoid typing the sys.
everytime for it), then you can use the from sys import argv statement. '''

from math import sqrt
print("The sqaure root of 16 is - ", int(sqrt(16)))

'''WARNING: In general, avoid using the from..import statement, use the import
statement instead. This is because your program will avoid name clashes and will be
more readable. '''


# We can use this to make the module behave in different ways depending on whether it is being used by itself or being imported
# from another module. This can be achieved using the __name__ attribute of the module

if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')


