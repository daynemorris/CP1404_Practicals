"""
CP1404 - Capitalist Conrad
Dayne Morris
"""

import random

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 0.01
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0

days_elapsed = 0

OUTPUT_FILE = "output_file.txt"
out_file = open(OUTPUT_FILE, 'w')

price = INITIAL_PRICE
print("${:,.2f}".format(price))

while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    days_elapsed = days_elapsed + 1
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    print("On day {} price is: ${:,.2f}".format(days_elapsed, price), file=out_file)

out_file.close()
