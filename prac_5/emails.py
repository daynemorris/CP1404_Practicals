"""
Emails
Estimate: 30 minutes
Actual: 45 minutes
"""


def main():
    emails_to_names = {}
    emails = input("Enter Email: ")
    while emails != "":
        name = get_name(emails)
        name_confirmation = input(f"Is your name {name}? (Y/n) ")
        if name_confirmation.upper() != "Y" and name_confirmation != "":
            name = input("Name: ")
        emails_to_names[emails] = name
        emails = input("Enter Email: ")
    for email, name in emails_to_names.items():
        print(f"{email} ({name})")


def get_name(emails):
    prefix = emails.split('@')
    name_parts = prefix.split('.')
    name = " ".join(name_parts).title()
    return name


main()
