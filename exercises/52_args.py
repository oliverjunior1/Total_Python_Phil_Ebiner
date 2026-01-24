# Create a function called sum_squares that takes any number of numeric arguments, and returns the sum of their values
# squared.
#
# For example for the arguments sum_squares(1,2,3) it should return 14 (1+4+9).

def sum_squares(*args):
    sum = 0
    for arg in args:
        sum += arg**2
    return sum

print(sum_squares(1,2,3))