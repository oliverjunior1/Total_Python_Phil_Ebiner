# Remove the characters to the left of our main text:
#
# ,
#
# :
#
# %
#
# _
#
# #
#
# Use the lstrip() method. Print the result to the screen:
#
# ",:_#,,,,,,:::____##Total_ _Pyt%on,,,,,,::#"
#
# Search the documentation for the requested method to learn how it works. You can use intermediate variables if you need them.

characters = ",:_#,,,,,,:::____##Total_ _Pyt%on,,,,,,::#"

without_characters =characters.lstrip(',:_#%')

print(without_characters)

