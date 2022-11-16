"""
CP1404/CP5632 Practical - Modify Existing GUI Program
Box layout demo
Dayne Morris, JCU
"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle greet button press, update text input with user input."""
        print("test")
        self.root.ids.output_label.text = "Hello "
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def press_clear(self):
        """ Clear any buttons that have been selected (visually) and reset status text :return: None."""
        self.root.ids.output_label.text = " "
        self.root.ids.input_name.text = " "


BoxLayoutDemo().run()
