first_number = input('First Number: ')
second_number = input('Second Number: ')

while True:

    if first_number == 'q':
        break

    else:
        try:
            divider = int(first_number) // int(second_number)
            print(divider)
            break

        except:
            print('Second Number cannot be zero.')
            break