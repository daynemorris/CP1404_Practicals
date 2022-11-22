from prac_9.car import Car
import random


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        """Initialise an Unreliable Car instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive an Unreliable Car a certain distance, based on reliability."""
        random_number = float(random.randint(1, 100))
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven


