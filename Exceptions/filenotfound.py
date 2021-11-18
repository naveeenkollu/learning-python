
# def count_words(filename):
#     try:
#         with open(filename, encoding='utf-8') as file:
#             contents = file.read()

#     except FileNotFoundError:
#         print(f"File {filename} not found in directory.")

#     else:
#         words = contents.split()
#         num_words = len(words)
#         print(f"The file {filename} has about {num_words} words.")

# filenames = ["gatsby.txt", "siddhartha.txt", "metamorphsis.txt", 'moby_dick.py']

# for file in filenames:
#     count_words(file)

# common_words.py

def word_counter(filename, word):

    try:
        with open(filename, encoding='utf-8') as file:
            contents = file.read()

    except FileNotFoundError:
        pass

    else:
        word_count = contents.lower().count(word)
        print(f"We found {word_count} occurences of '{word}' in {filepath}.")

filepath = 'Exceptions\\gatsby.txt'
word_counter(filepath, 'the')




