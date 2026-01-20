# Create a function (count_even) that counts the number of even numbers
# that exist in a list (numbers), and returns the result of said count.

def count_even(numbers):
    even = []
    for x in numbers:
        if x % 2 == 0 and x>0:
            even.append(x)
        number = len(even)
    return number
numbers = [1,50,502,755,34]
print(count_even(numbers))