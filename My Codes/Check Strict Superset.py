setA = set(map(int, input().strip().split()))
x = 0

def strict_super_set(nset):
    if len(nset.difference(setA)) == 0 and len(setA.difference(nset)) != 0:
        return 0
    else:
        return 1


for i in range(int(input())):
    nset = set(map(int, input().strip().split()))
    m = strict_super_set(nset)
    x = x + m
if x == 0:
    print("True")
else:
    print("False")


