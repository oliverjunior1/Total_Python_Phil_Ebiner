def test(number1, number2, *args, **kwargs):

    print(f"The fist number is {number1}")
    print(f"The second number is {number2}")

    for arg in args:
        print(f"arg = {arg}")

    for key, value in kwargs.items():
        print(f"{key} = {value}")

args = [100,200,300,400]
kwargs = {'x':'one', 'y':'two', 'z':'three'}

test(15,50,*args, **kwargs)