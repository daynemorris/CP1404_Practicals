"""
CP1404 - Files
Dayne Morris
"""

NAME_FILE = "name_file.txt"

# User enters name and is stored in the file "name_file.txt"
name_file = open(NAME_FILE, 'w')
name = str(input("Enter your name: "))
print(name, file=name_file)
name_file.close()

# Open the file and read the name, then print "Your name is _____"
name_in_file = open(NAME_FILE, 'r')
name = name_in_file.read().strip()
name_in_file.close()
print("Your name is ", name)

# Open "numbers.txt" read the first two lines and print the sum
numbers_file = open("numbers.txt", 'r')
number1 = int(numbers_file.readline())
number2 = int(numbers_file.readline())
numbers_file.close()
print(number1 + number2)

# Print all lines in "numbers.txt" or any number of numbers
total = 0
numbers_file = open("numbers.txt", 'r')
for line in numbers_file:
    number = int(line)
    total = total + number
numbers_file.close()
print(total)
