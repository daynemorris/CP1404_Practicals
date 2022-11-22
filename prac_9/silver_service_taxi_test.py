"""
CP1404/CP5632 Practical - Suggested Solution
SilverServiceTaxi class tests
"""

from prac_9.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi."""
    taxi = SilverServiceTaxi("Taxi One", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())


main()
