
def find_max(num):
    max=0
    for item in num:
        if item>max:
            max=item
    return max

cd=[]
i=0
while i!=5:
    cd.append(int(input("Enter number > ")))
    i+=1
print(find_max(cd))

