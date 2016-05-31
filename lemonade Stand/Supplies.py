from Vendor import Vendor


class Supplies:
    def __init__(self, playerPurse, buyLemons, buySugar, buyIce, buyCups):
        self.lemons = 0
        self.sugar = 0
        self.ice = 0
        self.cups = 0
        self.playerPurse = playerPurse

    def buyLemons(self):
        vendor = Vendor(self.playerPurse)
        input = int(input("How many lemons do you want to buy? "))
        self.lemons += vendor.supplyLemons(input)

    def buySugar(self):
        vendor = Vendor(self.playerPurse)
        input = int(input("How much sugar do you want to buy? "))
        self.sugar += vendor.supplySugar(input)

    def buyIce(self):
        vendor = Vendor(self.playerPurse)
        input = int(input("How much ice do you want to buy? "))
        self.ice += vendor.supplyIce(input)

    def buyCups(self):
        vendor = Vendor(self.playerPurse)
        input = int(input("How many cups do you want to buy?"))
        self.cups += vendor.supplyCups(input)

    def useLemons(self, quantity):
        self.lemons -= quantity

    def useSugar(self, quantity):
        self.sugar -= quantity

    def useIce(self, quantity):
        self.ice -= quantity

    def useCups(self, quantity):
        self.cups -= quantity

