"""
CP1404 - Exceptions Demo
Dayne Morris
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator != 0:
        fraction = numerator / denominator
        print(f"{fraction}")
    else:
        print(f"Do not divide by zero")
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print(f"Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print(f"Cannot divide by zero!")
print(f"Finished.")

