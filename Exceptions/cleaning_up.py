try:

    file = open('handling_exceptions.py')
    # Here we are opening the file named 'handling_exceptions.py' and need to close the resource as soon as 
    # task is completed.

    age = int(input("Age: "))
    # Only accepts the type of 'int' or else raises an exception.
    xfactor = 10 / age
    # Only accepts the value of type 'int' but not 0.

    # file.close()
    # If I place file.close() here. We have a problem. 
    # If the execution of 'try' block raised an exception, then file.close() will not be executed goes directly to 'except'

except (ValueError, ZeroDivisionError):
    print('Oh! Enter valid number')

    # file.close()
    # I have a problem here too. 
    # When I place file.close() in 'except' block. The program starts execution starting from 'try' block and
    # if it doesn't raise any exception. Python skips the 'except' block and file.close() will not be executed.
    # Hence the file will not be closed.

else:
    print("You're code seems fine.")

    # file.close()
    # By placing in 'else'. Iam just duplicating the file.close() and makes the code not at all clean.
    # To satisfy all these problems. I use 'finally' keyword which will be executed at any cost.

finally:
    file.close()
