# Using the range() function, create in a single line of code a list
# consisting of all numbers that are multiples of 3 from 3 to 300
# (inclusive). Store this list in the variable my_list.

my_list = []

for x in range(3,301):
    if x % 3 == 0:
        my_list.append(x)

print(my_list)
