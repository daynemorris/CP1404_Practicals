"""
CP1404/CP5632 Practical - Suggested Solution
Programming Language class with tests.
"""


class ProgrammingLanguage:
    """Programming Language class for storing information about languages."""

    def __init__(self, name, typing, reflection, year):
        """Create a ProgrammingLanguage from attributes."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a representation of ProgrammingLanguage"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if a language is dynamically typed."""
        return self.typing == "Dynamic"
