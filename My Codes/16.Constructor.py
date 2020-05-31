
# Constructors is called at the time of creating object.
class point:
    def __init__(self, x, y): # we need add special method or function called constructor
        self.x=x
        self.y=y
    def move(self):
        print("Move")
        print(self.x)
    def draw(self):
        print("draw")

point=point(10, 20)
point.draw()
point.move()
print(point.x, point.y)
