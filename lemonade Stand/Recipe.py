#from Supplies import Supplies
class Recipe:

    def __init__(self):
        self.lemons =0
        self.sugar = 0
        self.ice = 0
        self.pitcher = 0

    def getRecipe(self):
        if self.lemons <= 5 and self.sugar == range(7,10):
            return (sweetLemonade)
        elif self.lemons == range(7, 10) and self.sugar <= 5:
            return (tartLemonade)
        elif self.lemons == 5 and self.sugar == 5:
            return (regLemonade)
        else
            return (badLemonade)



