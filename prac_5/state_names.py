"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
for code, name in CODE_TO_NAME.items():
    print(f"{code} is {name}")

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        code = CODE_TO_NAME.get(state_code)
        print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:
        print(f"Invalid short state")
    state_code = input("Enter short state: ").upper()
