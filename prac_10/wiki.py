import wikipedia


def main():
    user_input = input("Enter Page Title: ")
    while user_input != "":
        try:
            page = wikipedia.page(user_input, auto_suggest=False)
            title = page.title
            summary = page.summary
            print(f"Page: {page}")
            print(f"Title: {title}")
            print(f"Summary: {summary}")
        except wikipedia.DisambiguationError:
            print("Can't use that keyword")
        user_input = input("Enter Page Title: ")
    print("Carpe Diem!")


main()
