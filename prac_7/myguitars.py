from prac_6.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read file of Guitar details, save as objects, display and save."""
    print("\nList of Guitars:\n")
    guitars = load_guitars()
    for guitar in guitars:
        print(guitar)

    print("\nAdd a Guitar!\n")

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

    for guitar in guitars:
        print(guitar)
    save_guitars(guitars)


def load_guitars():
    """Load file of Guitars as a list of objects."""
    guitars = []
    in_file = open(FILENAME, 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], parts[1], parts[2])
        guitars.append(guitar)
        guitars.sort()
    return guitars


def save_guitars(guitars):
    """Save list of objects as a string to the file."""
    with open(FILENAME, 'w', encoding="utf-8") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


main()
