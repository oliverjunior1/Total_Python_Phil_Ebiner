def a_sum(*args):
    total = 0

    for arg in args:
        total += arg

    return total

print(a_sum(5,6,7))