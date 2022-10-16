"""
CP1404/CP5632 Practical
Hex Colours
"""

COLOUR_TO_CODE = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff",
                  "Alizarin crimson": "#e32636",
                  "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc", "AntiqueWhite": "#faebd7",
                  "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc"}

colour_code = input("Enter colour name: ").title()
while colour_code != "":
    try:
        code = COLOUR_TO_CODE.get(colour_code)
        print(colour_code, "is", code)
    except KeyError:
        print(f"Invalid colour name")
    colour_code = input("Enter colour name: ").title()
