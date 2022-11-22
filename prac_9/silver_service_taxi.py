from prac_9.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness



