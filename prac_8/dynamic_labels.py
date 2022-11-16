"""
CP1404/CP5632 Practical - Do-from-scratch Exercises
Dynamic Labels
Dayne Morris, JCU
"""


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    """Main program - Kivy app to demo dynamic label program."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = {"Anthony Kiedis", "Chad Smith", "Flea", "John Frusciante"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create buttons from the list of strings and add them to the GUI."""
        for name in self.names:
            temp_label = Label(text=name, font_size="48")
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
