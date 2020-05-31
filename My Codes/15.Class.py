# Always make Class name first char as capital char and there should not be space and underscore
############ CLASS must have something in body, there can't be empty class
class Pnum:
    def square(self):
        print("Square")
    def triple(self):
        print("triple")


result=Pnum()
result.x=5
result.y=10
result.square()
result.triple()
