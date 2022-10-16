
"""
Word Occurrences
Estimate: 20 minutes
Actual:    minutes
"""
words_to_number = {}
words = input("Text: ").split()
for word in words:
    amount_of_words = words_to_number.get(word, 0)
    words_to_number[word] = amount_of_words + 1
for word, number in words_to_number.items():
    print(f"{word} : {number}")

