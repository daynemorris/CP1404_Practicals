"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Read subject data and display properly."""
    data = get_data()
    display_detail(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subjects = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        subjects.append(parts)
        print("----------")
    input_file.close()
    return subjects


def display_detail(data):
    """Display data with proper formatting."""
    print("----------")
    for i in data:
        print("{} is taught by {} and has {} students".format(i[0], i[1], i[2]))


main()
