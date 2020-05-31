# create a class and class should have name attribute and talk function

class liveChat:
    def __init__(self, name):
        x=self.name=name
        print(self)
        print(x)
    def talk(self):
        print(f"Hello {self.name}, It was nice to talk to you")
        print(self)

live=liveChat(input("Write your name > "))
live.talk()
