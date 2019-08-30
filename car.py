class Car(object):

    def __init__(self, make, year, price):
        self.__make = make
        self.__year = year
        self.__price = price

    def setMake(self, make):
        self.__make = make

    def getMake(self):
        return self.__make

    def setYear(self, year):
        self.__year = year

    def getYear(self):
        return self.__year

    def setPrice(self, price):
        self.__price = price

    def getPrice(self):
        return self.__price

    def __eq__(self, car):
        return  self.__make == car.getMake() and
                self.__year == car.getYear() and
                sefl.__price == car.getPrice()
