#if you break out of a for or while loop, any corresponding loop, else block is not executed.
while True:
    s=input("Type your name = ")
    if s=="Eva":
        print("She is my lovely daughter")
        break
    print("Length of your name is ", len(s))
print("Break is over")

#break and continue statement can be used with the for loop as well.

while True:
    s=input("Enter the string = ")
    if s=="Eva":
        print("She is my lovely daughter")
        break
    if len(s)<3:
        print("Typer more character")
        continue
        # Continue send the command to starting point, and below line will not be displayed uuntill continue is executed
    print("it will start again")
else:
    print("Continue is over")




