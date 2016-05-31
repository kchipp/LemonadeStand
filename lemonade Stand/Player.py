from Purse import Purse
class Player:

    def __init__(self):
        self.name = None
        self.money = 20.00

    def namePlayer(self):
        player = input("New Player: Please Enter your Name ")
        player = player.lower()
        self.name = player



