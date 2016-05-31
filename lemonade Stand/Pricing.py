class Pricing:

    def __init__(self, player):
        self.player = player
        self.playerChoice = none

    def setPrice(self):
        playerChoice = input("What do you want to charge per cup of lemonade? ")
        aValidChoice = self.validateChoice(playerChoice)
        if aValidChoice == True:
            self.playerChoice = playerChoice
        else:
            print("Please enter a valid choice")
            setPrice(input)

    def validateChoice(playerChoice):
        if playerChoice == float(range(10,100)):
            return True
        else:
            return False

