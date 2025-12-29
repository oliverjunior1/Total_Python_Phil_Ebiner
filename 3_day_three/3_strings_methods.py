text = "We are going to learn six methods today"
result = text.upper()
result2 = text[4].upper()
result3 = text.lower()
# If you put something into split, that will be the separator for the new list created.
# if you don't put something, the method will considerate the space.
result4 = text.split()

print(result)
print(result2)
print(result3)
print(result4)

a = "learning"
b = "Python"
c = "is"
d = "amazing"
# If you put something on the quotation marks, what you put will be among the separations.
e = " ".join([a, b, c, d])

print(e)

print(text.find("s"))

# That will be the first what will be replaced and the second what will be posted.
print(text.replace("six", "a lot of"))
