from prac_6.guitar import Guitar


def main():
    """Read file of programming language details, save as objects, display."""
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
    guitars = []
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], parts[1], parts[2])
        guitars.append(guitar)
        guitars.sort()
    return guitars


def save_guitars(guitars):
    out_file = open('guitars1.csv', 'w')
    for guitar in guitars:
        out_file.write


main()
