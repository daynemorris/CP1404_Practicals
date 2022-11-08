"""
CP1404/CP5632 Practical - Suggested Solution
Guitar program.
"""
from prac_6.guitar import Guitar


def main():
    """Guitar program that uses Guitar Class."""
    print("My guitars!")
    guitars = []
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        add_guitar = Guitar(name, year, cost)
        print(f"{add_guitar}\n")
        guitars.append(add_guitar)
        name = input("Name: ")
    print("\n...snip...\n")
    print("These are my guitars:")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    guitars.sort()
    for i, guitar in enumerate(guitars, 1):
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        else:
            vintage_string = ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")


main()
