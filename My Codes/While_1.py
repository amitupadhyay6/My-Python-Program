
num=9
run= True

print("Let\' play guessing.\n you have 3 attempt to guess the answer")

while run:
    guess=int(input("Guess your number = "))
    if guess == num:
        print("Bingo, Correct guess")
        # this causes the while loop to stop
        run=False
    elif guess<num:
        print("Little short")
    else:
        print("Little high")

else:
    print("the while lop is over")

print("Done")
