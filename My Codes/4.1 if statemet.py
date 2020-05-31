
w=input("Enter your weight = ")
S=input("Type K(KG) or L(LBS) = ")
w=int(w)
if S=="K" or S=="k":
    w=w* 2.205
    print(f"Your weight is {w} Pounds ")
else:
    w=w*0.454
    print(f"Your weight is {w} Kg")
