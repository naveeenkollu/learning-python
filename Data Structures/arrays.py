from array import array

numbers = array('f', list(range(21)))

print(numbers)

inserted = numbers.insert(22, 55)
print(inserted, numbers)

popped = numbers.pop()
print(popped)

removed = numbers.remove(4)
print(removed, numbers)