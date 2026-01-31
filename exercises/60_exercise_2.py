# Write a function (you can name it whatever you want) that takes any word as a parameter, and returns
# all of its unique letters (without repetition) in alphabetical order.
# For example, if when calling this function we pass the word 'entertaining', it should return
# ['a', 'e', 'g', 'i', 'n', 'r', 't']

def phrase(word):
    list_letters = []
    for x in word:
        list_letters.append(x)
    set_letters = sorted(set(list_letters))
    return set_letters

print(phrase('entertaining'))
print(phrase('pineapple'))




