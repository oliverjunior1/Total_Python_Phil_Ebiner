# To do the coding exercise below, you can choose different paths.
# While the correct path in programming is the one that returns the
# correct result, I encourage you to try applying list comprehension
# concepts to begin to assimilate them for the future. They can be very
# useful in your professional practice!
#
# Create an even_values list consisting of the numbers in the values
# list that (you guessed it!) are even.

values = [1, 2, 3, 4, 5, 6, 9.5]

even_values = [x for x in values if x%2==0]

print(even_values)