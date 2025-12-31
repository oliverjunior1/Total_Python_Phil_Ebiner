# type any text, a poem or anyone
from numpy.ma.core import append

text = input("type any text, a poem or anyone: ")
list_counted_out = []

# ask the user three letters
# TODO: store those letters in a list
letters = input("type three letters, with spaces: ")
letters_list = letters.split(" ")

# 1 - how many times appears each of those letters
# TODO: pass text and letters to lowercase
for x in letters_list:
    list_counted_out = append(x)
    print(list_counted_out)

# 2 - how many words in total

# TODO: use methods to transform it into a list of words to calculate its length

# 3 - first & last letter

# 4 - words in inverted order

# 5 - is 'python' there?


