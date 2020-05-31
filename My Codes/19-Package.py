# In a same way we can import the Package and then

print("Importing Package")
import Ecomerce.Module3
Ecomerce.Module3.credit_pack()

print("\nImporting Module3 from Package")
from Ecomerce import Module3
Module3.credit_pack()

print("\nImporting func from module of the package")
from Ecomerce.Module3 import credit_pack
credit_pack()
