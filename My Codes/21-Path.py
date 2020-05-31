# As P is in caps, Path is a class.
# Absolute path
    # c:\prog\micro\etc
# Relative path - you define some fix path then it will relate to  that

from pathlib import Path

path=Path("Ecomerce")
print(path.exists())
path=Path("ecomerce1")
print(path.exists(), path)

# Create directory
path=Path("New")
print(path.mkdir())
#Use below to delete the new path
#path=Path("New")
#path.rmdir()

path=Path()
for file in path.glob("*.py"): # argument define, hwich kind of file you want to search
    print(file)





