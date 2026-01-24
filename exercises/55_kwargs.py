# Create a function called number_attributes that counts the number of parameters that are passed, and returns that
# number as the result.

def number_attributes(**kwargs):
    return kwargs.items().__len__()

print(number_attributes(a=1, b=2, c=3, d=4))

