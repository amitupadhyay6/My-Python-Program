# inheritance is method to call function in other classes.

class Mammel:
    def walk(self):
        print("Walk")

class Dog(Mammel): # This is inheritance, we are inheriting the property of parent class.
    #Class must have some body, if not use "PASS" to pass to next line
    pass

class Cat(Mammel):
    def mu(self):
        print("Cat does MUMU")


dog1=Dog()
cat1=Cat()
dog1.walk()
cat1.walk()
cat1.mu()




