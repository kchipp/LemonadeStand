from GameIntro import GameIntro
from Player import Player
from Weather import Weather
from Temperature import Temperature
from Purse import Purse
#from Stand import Stand
#from Vendor import Vendor
#from Supplies import Supplies
#from Customer import Customer
from Pricing import Pricing


def Main():
    gameIntro = GameIntro()
    gameIntro.getIntro()
    player = Player()
    player.namePlayer()
    weather = Weather()
    weather.getWeather()
    print ("Today's weather forecast is %s." % (weather.weather))
    temperature = Temperature()
    temperature.getTemperature()
    print("Today's temperature will %s degrees." % (temperature.temperature))
    print("Let's get our supplies and make some lemonade.")
    price = Pricing()
    price.setprice()
    playerChoice.setPrice()




if __name__ == "__main__":
    Main()