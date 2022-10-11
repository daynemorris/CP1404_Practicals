"""
CP1404/CP5632 Practical
"'Quick Pick' Lottery Ticket Generator"
"""
import random

MINIMUM = 1
MAXIMUM = 45
NUMBERS_IN_LINE = 6


def main():
    """Get picks from user to determine quick picks and display them nicely."""
    user_picks = get_picks()
    quick_picks(user_picks)


def get_picks():
    """Get picks from the user."""
    user_picks = int(input("How many quick picks? "))
    return user_picks


def quick_picks(user_picks):
    """Determine quick picks from user_picks and display them nicely."""
    for i in range(user_picks):
        quick_pick = []
        for x in range(NUMBERS_IN_LINE):
            random_number = random.randint(MINIMUM, MAXIMUM)
            while random_number in quick_pick:
                random_number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(random_number)
        quick_pick.sort()
        print(" ".join(f"{random_number:2}" for random_number in quick_pick))


main()
