# Create a function called return_distincts() that receives 3 integers as parameters. If the sum of the 3 numbers is
# greater than 15, it must return the highest number.
# If the sum of the 3 numbers is less than 10, it must return the lowest number. If the sum of the 3 numbers is a value
# between 10 and 15 (included), then it must return the number with the intermediate value.
def return_disticts():
    num1 = int(input("Put the fist number: "))
    num2 = int(input("Put the second number: "))
    num3 = int(input("Put the third number: "))
    sum_numbers = num1 + num2 + num3
    if sum_numbers>15:
        if num1>num2 and num1>num3:
            print(num1)
        elif num2>num1 and num2>num3:
            print(num2)
        else:
            print(num3)
    elif sum_numbers <= 15 and sum_numbers>10:
        if num1<num2 and num1>num3:
            print(num1)
        elif num2<num1 and num2>num3:
            print(num2)
        else:
            print(num3)
    else:
        if num1<num2 and num1<num3:
            print(num1)
        elif num2<num1 and num2<num3:
            print(num2)
        else:
            print(num3)

return_disticts()






