from prac_9.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a representation of the Taxi string and flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall}"

    def get_fare(self):
        """Get new fare based on class variable flagfall."""
        return self.flagfall + super().get_fare()