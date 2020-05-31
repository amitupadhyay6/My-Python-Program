#while statement can have an optional else clause.

num=9
run= True

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

# Do anything else you want to do here
print("Done")

