
from Module2 import find_max

cd=[]
i=0
while i!=5:
    cd.append(int(input("Enter number > ")))
    i+=1

print(find_max(cd))
