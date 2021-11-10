numbers = list(range(11))
print(f"Original List: {numbers}")

first, *others, second = numbers
print(f"Unpacked List: {first} --> {second} --> {others}")
