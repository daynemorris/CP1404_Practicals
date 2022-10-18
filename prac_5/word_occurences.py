"""
Word Occurrences
Estimate: 20 minutes
Actual: 35 minutes 
"""
words_to_number = {}
text = input("Text: ")
words = text.split()
for word in words:
    amount_of_words = words_to_number.get(word, 0)
    words_to_number[word] = amount_of_words + 1

words = list(words_to_number.keys())
words.sort()

maximum_words = max(len(word) for word in words)
for word, number in sorted(words_to_number.items()):
    print(f"{word:{maximum_words}} : {number}")

