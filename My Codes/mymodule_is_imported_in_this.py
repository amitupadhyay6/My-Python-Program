# Imported two new module created in the lab

import mymodule
mymodule.say()
print("The version of my module is ", mymodule.__version__)

import Module1
print("\n", Module1.sys.path)
'''from mymodule import *
This will import all public names'''

#WARNING: Remember that you should avoid using import-star, i.e. from mymodule import *
