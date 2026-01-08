# Create a list formed by the tuples (index, element), obtained through enumerating the indices
# of each character of the "Python" string.
#
# Call the returned list with the variable name indices_list.

name = "Python"
indices_list = []

for element, index in enumerate(name):
    indices_list.append(element, index)

print(indices_list)