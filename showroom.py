from car import Car
import sys

class Showroom(object):

    def __init__(self):
        self.__cars = []
        self.__total_price = 0.0

    def addCar(self, car):
        self.__cars.append(car)
        self.__total_price += car.getPrice()

    def removeCar(self, car):
        try:
            self.__cars.remove(car)
            self.__total_price -= car.getPrice()
        except ValueError:
            print("Car not found in inventory")

    def calculateAveragePrice(self):
        # edge case: if the showroom has no car at all
        if len(self.__cars) == 0:
            return None
        # normal case
        return self.__total_price / len(self.__cars)

    def findTheOldestCar(self):
        oldest_car = None
        oldest_year = sys.maxint
        for car in self.__cars:
            if car.getYear() < oldest_year:
                oldest_car = car
                oldest_year = car.getYear()
        return oldest_car

    def findTheMostExpensiveCar(self):
        most_expensive_car = None
        most_expensive_price = sys.minint
        for car in self.__cars:
            if car.getPrice() > most_expensive_price:
                most_expensive_car = car
                most_expensive_price = car.getPrice()
        return most_expensive_car
