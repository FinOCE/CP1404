"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from car import Car # changed from "prac_06.car" to "car" for my project structure


def demo_code():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

def main():
    limo = Car('limo', 100)
    limo.add_fuel(20)
    print(limo.fuel)
    limo.drive(115)
    print(limo.odometer)
    print(limo)

main()