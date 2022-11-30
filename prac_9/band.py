"""
CP1404/CP5632 Practical
Band Class - Dayne Morris
"""


class Band:
    """Band class"""

    def __init__(self, name):
        """Initialise the Band using name attribute and list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of Band"""
        musicians_string = [str(musician) for musician in self.musicians]
        musicians_string = ", ".join(musicians_string)
        return f"{self.name} ({musicians_string})"

    def add(self, musician):
        """Add new musicians to list of musicians."""
        self.musicians.append(musician)

    def play(self):
        """Make each musician play."""
        # for musician in self.musicians:
        #     print(musician.play())    #kept returning None after last musician

        playing_musicians = [musician.play() for musician in self.musicians]
        playing_musicians = "\n".join(playing_musicians)
        return playing_musicians
