# guessing number
s=9
j=0
while j<3:
    g=int(input("guess the number = "))
    if g==s:
        print("You guessed it correctly")
        break
    else:
        j+=1
if j == 3:
    print("you are wrong")
##### use while and else funtion
j =0
while j<3:
    g=int(input("Guess the number = "))
    j+=1
    if g==s:
        print("Bingo, it is correct")
        break
else:
    print("Oops, you are wrong")
