### try except i used to handle the exceptiom
try:
    age=int(input("Age: "))
    print(age)
    income=8000
    age=0
    cd=income/age
    print(cd)
except ValueError:
    print("Invalid Value")
except ZeroDivisionError:
    print("Age can not be zero")
