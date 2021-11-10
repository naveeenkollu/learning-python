try:
    with open("app.py") as file:
        print("File opened.")
    # To avoid using 'finally', I can use 'with' clause which automatically opens and closes an external resource 
    # after execution.

    age = int(input("Age: "))

except ValueError:
    print("Enter valid input type of 'int'")

else:
    print("Executed perfectly!")

