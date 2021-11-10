# listed = ['a', 'b', 'c', 'b', 'd', 'b']

# # adding items into list
# listed.append('e')
# print(f"Appended List: {listed}")

# listed.insert(0, 'z')
# print(f"Inserted List: {listed}")

# # removing items from the list
# listed.pop()
# print(f"Popped list: {listed}")

# listed.pop(0)
# print(f"Popped list: {listed}")

# for letter in listed:
#     listed.remove('b')
#     print(f"Popped item: {listed}")

# del listed[:]
# print(f"Deleted List: {listed}")

# listed.clear()
# print(f"Popped list: {listed}")

# Removing empty strings from the list

# letters = ['a', 'b', 'c', 'b', 'd', 'e', 'b']

# for letter in letters:
#     current_list = letters.remove('b')

# print(f"Listing after removing duplicates: {current_list}")


numbers = [55, 22, 15, 2, 9, 33, 58]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)


