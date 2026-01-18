# Create a function (all_positives) that returns True if all the values in a list are positive, and False if at least
# one of the values is negative. Create a list named numbers with positive and negative values.
#
# Don't call the function, you just need to define it.
def all_positives(lst):
    """Return True if all values in the list are positive,
    otherwise return False."""
    for value in lst:
        if value < 0:
            return False
    return True

# Example list with positive and negative values
numbers = [3, -1, 7, 0, 12, -5]
