# Python has a nifty feature called documentation strings, usually referred to by its shorter
# name docstrings. DocStrings are an important tool that you should make use of since it
# helps to document the program better and makes it easier to understand. Amazingly, we can
# even get the docstring back from, say a function, when the program is actually running!
def PMax(a,b):
    #below is DocString
    ''' there are two integer number

    it will print the max value of the two integer value'''
    x=int(a)
    y=int(b)
    if x>y:
        print(x, " is maximum")
    else:
        print(y, " is maximum")

PMax(int(input("1st Num = ")) ,int(input("2nd Num = ")))
print(PMax.__doc__)
#Calling help of the function
help(PMax)

# The convention followed for a docstring is a multi-line string where the first line starts with a
# capital letter and ends with a dot. Then the second line is blank followed by any detailed
# explanation starting from the third line. You are strongly advised to follow this convention for
# all your docstrings for all your non-trivial functions.
