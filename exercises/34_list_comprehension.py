# To do the coding exercise below, you can choose different paths.
# While the correct path in programming is the one that returns the
# correct result, I encourage you to try applying list comprehension
# concepts to begin to assimilate them for the future. They can be
# very useful in your professional practice!
#
# Create a square_values list consisting of the numbers in the values
# list, squared.

values = [1, 2, 3, 4, 5, 6, 9.5]

square_values = [x**2 for x in values]

print(square_values)


