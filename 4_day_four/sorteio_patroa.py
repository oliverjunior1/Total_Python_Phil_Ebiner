import random


def lucky():
    x = list(sorted(random.sample(range(1,32),7)))

    print(x)

lucky()