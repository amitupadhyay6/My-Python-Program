def greet_user(name):
    print(f"Hello {name}, Good Morning")
    print("good day !!")

print("Start")
greet_user(input("Enter your name > "))
greet_user("Vibha") ########### positional Argument
print("end")

# we need to define before calling them.

# keyword agrument
def name_rec(name, age):
    print(name, age)
name_rec(age=31, name="amit") ########### Keyword Atgument and it should always come after the postional argument


