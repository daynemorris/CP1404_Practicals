"""
CP1404/CP5632 Practical
Test Unreliable Car
"""

from prac_9.unreliable_car import UnreliableCar


def main():
    """Test Taxi class."""
    first_car = UnreliableCar("Camry", 100, 30)
    second_car = UnreliableCar("Prius 1", 50, 10)

    for i in range(10):
        print(f"{first_car.name} drove {first_car.drive(i)}km with {first_car.fuel}")
        print(f"{second_car.name} drove {second_car.drive(i)}km with {second_car.fuel}")

    print(first_car)
    print(second_car)


main()
