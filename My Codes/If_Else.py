
#There are three control flow statements in Python - if , for and while .
num=23
guess=int(input("Guess the number = "))
#Int() function will store only the interger value
# input() function is to get input from user and input function which prints it to the screen and waits for
# input from the user.

if guess == num:
    # New block starts here
    #if statement contains a colon at the end - we are indicating to Python that a block of statements follows.
    print("Bingo");
    print("You Succeeded")
elif guess < num:
    # Another block starts here
    print("You are little short");
else:
    # Another block starts here
    print("You are little higher");
print("\n Game is over")
# This last statement is always executed,
# after the if statement is executed.

