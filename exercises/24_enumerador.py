# Create a list formed by the tuples (index, element), obtained through enumerating the indices
# of each character of the "Python" string.
#
# Call the returned list with the variable name indices_list.

name = "Python"
indices_list = []

for x in enumerate(name):
    indices_list.append(x)

print(indices_list)