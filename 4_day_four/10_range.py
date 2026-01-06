# Use the range() function and a loop to add the squares of all the
# numbers from 1 to 15 (inclusive). Store the result in a variable
# called sum_squares.
#
# For this purpose:
#
# Create a range of values that you can iterate through in a loop
#
# For each of these values, find its squared value (power of 2). You may
# need to create intermediate variables (optionally).
#
# Sum all the squared values obtained. Accumulate the sum in the variable
# sum_squares.
sum_squares = 0

for x in range(1,16):
    sum_squares += x**0.5
print(sum_squares)