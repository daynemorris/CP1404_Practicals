"""
CP1404 - Files
Dayne Morris
"""

NAME_FILE = "name_file.txt"

# Algorithm asks for users name and stores it in "name_file.txt"
name_file = open(NAME_FILE, 'w')
name = str(input("Enter your name: "))
print(name, file=name_file)
name_file.close()

# Open NAME_FILE for reading then print the name inside the file
name_in_file = open(NAME_FILE, 'r')
name = name_in_file.read().strip()
name_in_file.close()
print("Your name is ", name)

# Open "numbers.txt" file for reading. Read the first two lines then print the sum
numbers_file = open("numbers.txt", 'r')
number1 = int(numbers_file.readline())
number2 = int(numbers_file.readline())
numbers_file.close()
print(number1 + number2)

# Read all the lines in "numbers.txt" then print them or any numbers of numbers
total = 0
numbers_file = open("numbers.txt", 'r')
for line in numbers_file:
    number = int(line)
    total = total + number
numbers_file.close()
print(total)
