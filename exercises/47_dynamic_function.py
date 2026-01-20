# Create a function (sum_less) that adds the numbers of a list as long
# as they are greater than 0 and less than 1000, and returns the result
# of said sum. Create a numbers variable, storing a list of numbers so
# we can test it.

def sum_less(numbers):
    total = 0
    for n in numbers:
        if 0 < n < 1000:
            total += n
    return total


# List to test the function
numbers = [10, -5, 500, 1000, 250, 0, 1500, 30]

# Test
result = sum_less(numbers)
print(result)

