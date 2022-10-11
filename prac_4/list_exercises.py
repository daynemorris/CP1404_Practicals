"""
CP1404/CP5632 Practical
Basic List Operations
"""


def main():
    """Display numbers based on user input nicely and check user authorization."""
    numbers = get_numbers()
    display_numbers(numbers)
    determine_authorised_users()


def get_numbers():
    """Get numbers from users and store it in a list."""
    numbers = []
    for i in range(5):
        number = int(input("Number: "))
        numbers.append(number)
    return numbers


def display_numbers(numbers):
    """Display the numbers nicely."""
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average number is {}".format(sum(numbers) / len(numbers)))


def determine_authorised_users():
    """Get username and determine if said username in the auth list."""
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username = input("Enter Username: ")
    if username in usernames:
        print(f"Access granted")
    else:
        print(f"Access denied")


main()
