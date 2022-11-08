"""
CP1404/CP5632 Practical - Suggested Solution
Programming Language client code.
"""
from prac_6.programming_language import ProgrammingLanguage


def main():
    """Test for ProgrammingLanguage class"""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [python, ruby, visual_basic]
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
