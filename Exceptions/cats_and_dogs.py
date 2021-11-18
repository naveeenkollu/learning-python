filenames = ['Exceptions\cats.txt', 'Exceptions\dogs.txt']

for filename in filenames:

    try:
        with open(filename) as f:
            contents = f.read()

    except FileNotFoundError:
        pass

    else:
        print(contents)
