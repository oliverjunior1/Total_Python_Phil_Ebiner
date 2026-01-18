# Create a function (all_positives) that returns True if all the values in a list are positive, and False if at least
# one of the values is negative. Create a list named numbers with positive and negative values.
#
# Don't call the function, you just need to define it.
def all_positives(numbers):
    return numbers in range(-10000,0)

numbers = [10,15,20,18]
print(all_positives(numbers))
