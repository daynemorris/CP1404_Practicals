"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Get the number_of_months and add them to a list of incomes."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    print_report(incomes, number_of_months)


def print_report(incomes, number_of_months):
    """Display the report with formatting given the income and number_of_months."""
    total = 0
    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()
