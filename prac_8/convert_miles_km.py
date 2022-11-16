"""
CP1404/CP5632 Practical - Do-from-scratch Exercises
Miles to Kilometres Converter
Dayne Morris, JCU
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM_FACTOR = 1.609


class ConvertDistanceApp(App):
    """Convert distance app converts distances from miles to km."""
    output_km = StringProperty()

    def build(self):
        """build the Kivy app from the kv file """
        self.title = "Convert Distance"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self, text):
        """Handle calculation (could be button press or other call)."""
        print("handle calculate")
        miles = self.convert_to_number(text)
        self.update_result(miles)

    def handle_increment(self, text, change):
        """Handle up/down button press, update the text input with new value, call calculation function."""
        print("handle increment")
        miles = self.convert_to_number(text) + change
        self.root.ids.user_input.text = str(miles)

    def update_result(self, miles):
        print("update")
        self.output_km = str(miles * MILES_TO_KM_FACTOR)

    # The following line uses a static method so that convert_to_number is part of the class
    @staticmethod
    def convert_to_number(text):
        """Convert text to float or 0.0 if invalid."""
        try:
            return float(text)
        except ValueError:
            return 0.0


ConvertDistanceApp().run()
