"""
CP1404
Prac 3: String Formatting
Dayne Morris - 2/10/2022
"""

# PART 1: f-string formatting
name = "Gibson L-5 CES"
year = 1922
cost = 16035.4

print(f"{year} {name} for about ${cost}!")

# PART 2: using a loop to format
for i in range(0, 200, 50):
    print(f"{i:5}")
