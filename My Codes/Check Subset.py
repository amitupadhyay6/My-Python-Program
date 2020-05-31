
no_of_testcase = int(input())
for i in range(no_of_testcase):
    size_of_set_A = int(input())
    aset = set(map(int, input().strip().split()[:size_of_set_A]))
    size_of_set_B = int(input())
    bset = set(map(int,input().strip().split()[:size_of_set_B]))
    subset = aset.difference(bset)
    if len(subset) == 0:
        print("True")
    else:
        print("False")
