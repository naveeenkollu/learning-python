# try:
#     age = int(input("Age: "))
#     print(age)

# except ValueError as ex:
#     print("You didn't enter valid age")
#     print(ex)
#     print(type(ex))


# else:
#     print("No exceptions were thrown")
#     print("Entered correct value")

# When you run this program, it first executes the try clause and takes the input from the terminal.
# If the input provided is valid, prints out the output(age) & goes to else and prints out the statements.
# If the input provided is invalid, goes to except-clause and prints the terminal with cause of exception
# 
# CONTROL FLOW
# -------------
# 
# Run Program 
#      |
# Goes to 'try' & executes try block
#      |
# Takes input from user(terminal)
#      |
# if the input is type of 'int'. It prints the age and else block statements
#      |
# if the input is not type of 'int'. It goes to 'except' block and prints the terminal with exception message
# 
# 
# Try, except clause helps you to execute the remaining program without stopping the execution
# by just raising an exception message.
# 
# Helps to fix the program by knowing the cause of error.  


try:
    age = int(input("Age: "))
    xfactor = 10/age
    print(xfactor)

except (ValueError, ZeroDivisionError):
    print("Looks like you didn't entered a valid type.")

else:
    print('Your code working absolutely fine.')


# When try block is executed,the input entered by user,seems to be not valid then it goes to except block,
# matches one of two exceptions and prints the terminal with except message.

