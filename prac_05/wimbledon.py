"""
Wimbleon
Estimate: 50 minutes
Actual: 1hr 24 minutes
"""

import csv

FILENAME = "wimbledon.csv"


def main():
    """Read the file and then print Champions and their Countries from Wimbledon"""
    tennis_records = load_csv(FILENAME)
    champion_to_count, countries = process_csv(tennis_records)
    display_data(champion_to_count, countries)


def load_csv(filename):
    """Load records from csv into a list of lists"""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        reader = csv.reader(in_file)
        player_to_country = list(reader)
        return player_to_country


def display_data(champions_to_count, countries):
    """Display Champions and their Countries with proper formatting"""
    for champions, count in champions_to_count.items():
        print(f"{champions} {count}")

    print(f"\nThese {len(countries)} have won Wimbledon:")
    print(",".join(sorted(countries)))


def process_csv(tennis_records):
    """Make a dictionary and set of countries from the loaded csv file"""
    champions_to_count = {}
    countries = set()
    for record in tennis_records:
        countries.add(record[1])
        try:
            champions_to_count[record[2]] += 1
        except KeyError:
            champions_to_count[record[2]] = 1
    return champions_to_count, countries


main()
