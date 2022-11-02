"""
CP1404/CP5632 Practical - Suggested Solution
Guitar class
"""
CURRENT_YEAR = 2022
VINTAGE_NUMBER = 50


class Guitar:
    """Guitar class for storing details about a Guitar."""

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """Get the age of a guitar based on CURRENT_YEAR."""
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        """Determine if the guitar is Vintage or not based on VINTAGE_NUMBER"""
        if self.get_age() >= VINTAGE_NUMBER:
            return True
        else:
            return False

    def __lt__(self, other):
        """Less than, used for sorting Guitars - by year released."""
        return self.year < other.year
