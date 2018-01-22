def is_isogram(string):
    string = string.lower()
    letter_count = [string.count(letter) for letter in string if letter.isalpha()]
    return sum(letter_count) == len(letter_count)