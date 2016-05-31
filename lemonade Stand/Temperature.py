import random

class Temperature:
    
    def __init__(self):
        self.temperature = None

    def getTemperature(self):
        possibleTemperature = range(60,95)
        self.temperature = random.choice(possibleTemperature)

    def goodTemp(self):
        self.self.temperature == range(80, 95)

    def okTemp(self):
        self.self.temperature == range(70, 79)

    def badTemp(self):
        self.self.temperature < 69