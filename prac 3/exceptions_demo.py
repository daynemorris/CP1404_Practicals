"""
CP1404 - Practical
Answer the following questions:
1. When will a ValueError occur?
    when the value is != an integer
2. When will a ZeroDivisionError occur?
    when the denominator = 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
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

