from car import Car
import random as r

class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability
    
    def drive(self, distance):
        if r.randint(0, 100) < self.reliability:
            super().drive(distance)
        else:
            print(f'The car failed. How unreliable!')