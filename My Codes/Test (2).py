class IceCreamMachine:
    
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings
        
    def scoops(self):
        ab=[]
        cd={}
        for i in self.ingredients:
            ab.append(i)
        for i in ab:
            cd[ab[0]]=self.toppings
            cd[ab[1]]=self.toppings
        return cd

        

if __name__ == "__main__":
    machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
    print(machine.scoops()) #should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]
