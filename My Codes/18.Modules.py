# Use "import" to call other modules (different piece of code), need to use Module_Name.Function() to use the function.
# use "From Module_Name import.Function to call specefic function of the module only, not the whole module. Here you can directly call the function.

import Module ############ Import entire Module

Module.greet_user("John")
Module.name_rec("Ron", 31)

## You can directly access function of imported modules

from Module1 import greet_user  ######### Import Specefic Function from the module
from Module import name_rec


name_rec("Dumble", 108)
greet_user("Harmaini")

