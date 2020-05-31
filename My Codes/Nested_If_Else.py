#There are three control flow statements in Python - if , for and while .
#Must follow the indentation, both if should be in same line
num=23
guess=int(input("Guess the number = "))

if guess == num:

    print("Bingo")
    print("You Succeeded")
if guess < num:
        print("You are little lower")
else:

    print("You are little higher");
print("\n Game is over")
