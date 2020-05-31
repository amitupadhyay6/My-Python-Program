
import random


class Dice:
    def roll(self):
        x=random.randint(1,6)
        y=random.randint(1,6)
        return x,y # python will automatically convert the return as Tuple


d=Dice()
ab=d.roll()
print(ab)
ab=d.roll()
print(ab)
ab=d.roll()
print(ab)
ab=d.roll()
print(ab)



