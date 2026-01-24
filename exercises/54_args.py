# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite
# number of values.

def personal_numbers(name, *args):
    sum_numbers = 0
    for arg in args:
        sum_numbers += arg
    return f"{name}, the sum of your numbers is {sum_numbers}"

print(personal_numbers("Joaquim",1,2,3))