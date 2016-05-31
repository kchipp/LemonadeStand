class Vendor:
    def __init__(self, playerPurse):
        self.priceLemons = .11
        self.priceSugar = .10
        self.priceIce = .15
        self.priceCups = .25
        self.playerPurse = playerPurse

    def supplyLemons(self, numberOfLemons):
        self.playerPurse.money -= (numberOfLemons * self.priceLemons)
        return (numberOfLemons)

    def supplySugar(self, numberOfSugar):
        self.playerPurse.money -= (numberOfSugar * self.priceSugar)
        return (numberOfSugar)

    def supplyIce(self, numberOfIce):
        self.playerPurse.money -= (numberOfIce * self.priceIce)
        return (numberOfIce)

    def supplyCups(self, numberOfCups):
        self.playerPurse.money -= (numberOfCups * self.priceCups)
        return (numberOfCups)