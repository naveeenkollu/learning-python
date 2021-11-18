# file_path = "D:\Python\Files\pi_digits.txt"

# with open(file_path) as file:
#     lines = file.readlines()

# pi_string = ''

# for line in lines:
#     pi_string += line.rstrip()

# print(pi_string)

# birthday = input('Enter your birthday date in DD-MM-YYYY: ')

# if birthday in pi_string:
#     print(f"You're birthday is in pi value")

# else:
#     print(f"Not found!")

# file_path = 'D:\Python\Files\learning_python.txt'

# with open(file_path) as file:
#     lines = file.readlines()
# # print(lines * 3)

# # print('\n')

# # for line in lines:
# #     print(line.rstrip())

# string_sentence = ''

# for line in lines:
#     string_sentence += line
# print(string_sentence.rstrip())


"""
    open(filename, filemode)
    
    File modes:
    -----------
    r - read - reads the data from the file
    w - write - writes data to the file
    a - append - writes data to the file at the end without erasing existing data
    r+ - read, write - can read and write at same time
"""

# file_path = 'D:\Python\Files\learning_c.txt'

# with open(file_path, 'a') as file:
#     contents = file.write('I love Programming.\n')
#     contents = file.write('I love Python.\n')
# print(contents)


# file_path = 'D:\Python\Files\guest_book.txt'

# while True:

#     name = input('Tell your name: ')
#     contact = int(input('Contact No: '))

#     if name == 'quit':
#         break

#     else:
#         with open(file_path, 'a') as file:
#             file.write(f"{name} - {contact}\n")
#             print(f"Hi {name}, We added your contact to the guest book.")

file_path = 'D:\Python\Files\poll.txt'

while True:

    name = input('What is your name?\n')
    response = input('Why do you like programming?\n')

    if name == 'quit' or response == 'quit':
        break
    else:

        with open(file_path, 'a') as file:
            file.write(f"{name} - {response}\n")
            print("You're response has been recored")