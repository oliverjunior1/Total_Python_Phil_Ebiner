def a_sum(**kwargs):
    total = 0
    for key, value in kwargs.items():
        print(f'{key} = {value}')
        total += value
    return total


a_sum(a=3, y=5, z=2)
