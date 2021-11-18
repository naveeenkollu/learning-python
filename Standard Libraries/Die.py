from random import randint, choice

# class Die():

#     def __init__(self, sides=6):
#         self.sides = sides

#     def roll_die(self):
#         return randint(1, self.sides)

# die_6 = Die()

# result = []

# for rollnum in range(10):
#     rolled = die_6.roll_die()
#     result.append(rolled)
# print(f"Dice with 6-sides: {result}")

# die_10 = Die(sides=10)

# result = []

# for rollnum in range(10):
#     rolled = die_10.roll_die()
#     result.append(rolled)
# print(f"Dice with 10-sides: {result}")

# die_20 = Die(sides=20)

# result = []

# for rollnum in range(10):
#     rolled = die_20.roll_die()
#     result.append(rolled)
# print(f"Dice with 20-sides: {result}")

class Lottery():
    def __init__(self):
        self.number_picker = []

    def magic_number(self):
        lottery_number = ''

        for num in range(5):
            picked = self.number_picker
            picked.randint()
        



lottery = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D']
print(lottery)
