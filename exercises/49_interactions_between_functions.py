# Create a function (throw_dice) that "throws" two random dice and
# returns its results (the function MUST RETURN TWO VALUES AS A RESULT,
# both of which must be between 1 and 6, randomly).
import random


def throw_dice():
    roll_1 = random.randint(1,6)
    roll_2 = random.randint(1,6)
    return  roll_1, roll_2

# Pass the result of these two dice to a function called roll_result (meaning that this second function MUST RECEIVE
# TWO ARGUMENTS) and return -without printing it- a certain message according to the what the sum of these values
# results:
def roll_result():
    x, y = throw_dice()
    sum_dice = x + y
    # sum_dice = rolls[0] + rolls[1]


# If the sum is less than or equal to 6:
    if sum_dice <=6:
        print(f"The sum of your dice is {sum_dice}. Unfortunate")

# If the sum is greater than 6 and less than 10:
    elif sum_dice > 6 and sum_dice<10:
        print(f"The sum of your dice is {sum_dice}. You have a good chance")

# If the sum is greater than or equal to 10:
    else:
        print(f"The sum of your dice is {sum_dice}. It looks like a winning roll")

# Hint: use the random library's choice or randint method to choose a
# random value between 1 and 6.

roll_result()

