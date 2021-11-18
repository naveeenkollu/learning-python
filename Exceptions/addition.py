while True:

    first_num = int(input('first number: '))
    second_num = int(input('second number: '))

    try:
        answer = first_num + second_num
        
    
    except ValueError:
        print("'string' is not allowed")

    else:
        print(f"Answer: {answer}")
        