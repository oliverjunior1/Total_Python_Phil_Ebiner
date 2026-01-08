# Print to the screen only the indices of those names in the list below, that start with M:
#
# You can solve it in different ways, but it will help you keeping mind some (if not all) the
# following elements:
# loops
# if conditionals
# the enumerate() method
# string methods and indexing

list_names = ["Maverick", "Alice", "Madeline", "Hazel", "Jack", "Meadow", "Thomas", "Emily", "Mills"]

for x, y in enumerate(list_names):
    if y.lower().startswith('m'):
        print(x)
    else:
        pass

