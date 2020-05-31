
x=1000000
has_good = 1

if has_good:
    p=0.1*x
else:
    p=0.2*x
print(f"Down Payment for the house is ${p}")

# logical and or NOT operator
has_h_i = 1
has_g_c = 1
if has_g_c and has_h_i:
    print("get away from loan's money")
if has_g_c or has_h_i:
    print("you will get approval after approval's ")
h_cri_re = 0
if has_g_c and not h_cri_re:
    print("good to go")
#######################################################

name= "Amit"
l=len(name)
if l < 3:
    print("name is having less 3 char")
elif l > 5:
    print("name is having more than 5 char")
else:
    print("name is good to go")
