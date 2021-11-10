# unpacking lists

numbers = list(range(1, 6))
print(*numbers)

# unpacking and combining lists
even_num = [number for number in range(21) if number % 2 == 0]
odd_num = [number for number in range(21) if number % 2 != 0]
print(f"Even: {even_num}")
print(f"Odd: {odd_num}")

numbers = [*even_num, *odd_num]
numbers.sort()
print("Unpacked numbers: ", *numbers)

# unpacking sets
numbers_1 = {range(1, 6)}
print(*numbers)

# unpacking & combining sets
even_num = {number for number in range(21) if number % 2 == 0}
odd_num = {number for number in range(21) if number % 2 != 0}

numbers = {*even_num, *odd_num}
print("unpacked numbers set:", *numbers)

# unpacking dictionaries
even_numbers = {'x': 2, 'y': 4}
odd_numbers = {'a': 1, 'b': 3}

numbers = {**even_numbers, **odd_numbers}
print(numbers)

