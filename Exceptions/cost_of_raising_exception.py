# The cost of raising an exception when you are building a large application cannot effective way to do. 
# Then raising an exception can be costly and degrades the performance. Before raising an exception think twice.
# If the exception can be solved using simple if - else codition then go for it
# or Write meaningful exceptions.

from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
            
    return 10 / age

try:
    calculate_xfactor(-1)

except: 
    pass
""" 



code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
            
    return 10 / age

xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
""" 

first_code = timeit(code1, number=10000)
second_code = timeit(code2, number=10000)

print("first code: ", first_code)
print("second code: ", second_code)

time_difference = first_code - second_code

if time_difference:
    print('Performance Bump by', time_difference)

else:
    print('No Performance Bump!')

