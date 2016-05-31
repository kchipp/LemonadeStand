import random
class Weather:

    def __init__(self):
        self.weather = None

    def getWeather(self):
        possibleWeather = ["Sunny", "Rain", "Cloudy"]
        self.weather = random.choice(possibleWeather)
