from Player import Player
#from Pitcher import Pitcher
from Vendor import Vendor
from Supplies import Supplies

class Stand:
    def __init__(self):
        self.player = Player()


    def buySupplies(self):
        buyLemons = input("Your current inventory is %s.  How many lemons would you like to buy " % (numberOfLemons))
        buySugar = input("Your current inventory is %s.  How much sugar would you like to buy? " % (numberOfSugar))
        buyIce = input ("Your current inventory is %s.  How much ice would you like to buy? " % (numberOfIce))
        buyCups = input ("Your current inventory is %s.  How many cups would you like to buy? " % (numberOfCups))

    def makeLemonade(self):
        recipeChoice = input("Which recipe do you want to use? Enter Sweet, Tart, or Regular ")
        self.pitcher.append(Pitcher(recipeChoice))

    def sellLemonade(self):
        priceLemonade = input("What do you want to charge per cup? ")
        self.pitcher




