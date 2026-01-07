# Print sentences like the following on the screen:
#
# '{name} is found at index {index}'
#
# Where name must be each of the names in the list below, and the index, must be obtained via enumerate().
#
# list_names = ["Steven", "Jackie", "Donna", "Kelso", "Eric", "Fez", "Kitty", "Red"]
#
# You can use the given print() line as an example and change its variable names, but the returned phrases must be the same!
#
# Tip: use loops!

list_names = ["Steven", "Jackie", "Donna", "Kelso", "Eric", "Fez", "Kitty", "Red"]

for index, name in enumerate(list_names):
    print(f'{name} is found at index {index}')