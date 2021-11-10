# Character Frequency - write a program to check how many times each character is repeated.
from pprint import pprint

sentence = "If you only read the books that everyone else is reading, you can only think what everyone else is thinking."

char_frequency = {}

for char in sentence:
    if char in char_frequency:
        char_frequency[char] = char_frequency[char] + 1

    else:
        char_frequency[char] = 1

pprint(char_frequency)