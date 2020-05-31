import random

n=3
if n%2==0:
    if n in range(2,5):
        print("Not Weird")
    elif n in range(6,20):
        print("Weird")
    elif n in range(20,99):
        print("Not Weird")
else:
    print("Weird")

n=24
if n%2==0:
    if n in range(2,5):
        print("Not Weird")
    elif n in range(6,20):
        print("Weird")
    elif n in range(20,99):
        print("Not Weird")
else:
    print("Weird")
