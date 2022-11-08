"""
CP1404/CP5632 Practical - Suggested Solution
Basic manual tests for Guitar class
"""

from prac_6.guitar import Guitar


def main():
    """Tests for the Guitar class."""
    guitar = Guitar(name="Gibson L-5 CES", year=1922, cost=16035.40)
    another_guitar = Guitar(name="Another Guitar", year=2013, cost=15000)
    print(f"{guitar.name} get_age() - Expected {guitar.get_age()}. Got {guitar.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected {another_guitar.get_age()}. Got {another_guitar.get_age()}")
    print(f"{guitar.name} is_vintage() - Expected {guitar.is_vintage()}. Got {guitar.is_vintage()}")
    print(
        f"{another_guitar.name} is_vintage() - Expected {another_guitar.is_vintage()}. Got {another_guitar.is_vintage()}")


main()
