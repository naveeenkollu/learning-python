def calcuate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
        # Raising an exception when the argument passed to this function is zero or less than zero. 
        
    return 10 / age

try:
    calcuate_xfactor(-1)

except ValueError as error: 
    print(error)
