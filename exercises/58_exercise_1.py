# Create a function called return_distincts() that receives 3 integers as parameters. If the sum of the 3 numbers is
# greater than 15, it must return the highest number.
# If the sum of the 3 numbers is less than 10, it must return the lowest number. If the sum of the 3 numbers is a value
# between 10 and 15 (included), then it must return the number with the intermediate value.

def return_distincts(*args):
    sum = 0
    list_min_max = []
    list_2 = []
    for arg in args:
        list_min_max.append(arg)
        list_2 = sorted(list_min_max)
        sum += arg
        if sum > 15:
            return list_2[-1]
        elif 15 >= sum > 10:
            return list_2[1]
        else:
            return list_2[0]

num1 = int(input("Put the number one: "))
num2 = int(input("Put the number two: "))
num3 = int(input("Put the number three: "))

print(return_distincts(num1, num2, num3))


