# Create a function called return_distincts() that receives 3 integers as parameters. If the sum of the 3 numbers is
# greater than 15, it must return the highest number.
# If the sum of the 3 numbers is less than 10, it must return the lowest number. If the sum of the 3 numbers is a value
# between 10 and 15 (included), then it must return the number with the intermediate value.
def return_distincts(a, b, c):
    sum = a + b + c
    list = [a, b, c]
    if sum>15:
        print(max(list))
    elif sum<10:
        print(min(list))
    else:
        print(a + b + c - min(a, b, c) - max(a, b, c))

return_distincts(15,3,2)
return_distincts(1,2,3)
return_distincts(10,3,2)
return_distincts(15,25,10)





