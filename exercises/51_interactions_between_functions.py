# You must create a list with values and call it secret_codes.
import random

secret_codes = []
# Create a function called toss_coin that returns the result of a random coin toss. Such a function must be able to
# return the results "Heads" or "Tails", and must not receive any arguments to work.
def toss_coin():
    coin = ["Heads", "Tails"]
    throw_coin = random.choice(coin)
    return throw_coin
result_toss_coin = toss_coin()
# Create a second function called luck, that takes two arguments: the first must be the result of the coin toss. The
# second argument will be any list (the secret_codes variable that was created at the beginning).
def luck(result_toss_coin, secret_codes):

# If the coin comes up "Tails", luck should print this message to the user: "List will self-destruct", and return said
# list as empty list = [ ].
    if result_toss_coin=="Tails":
        print("List will self-destruct")
        return secret_codes.clear()
# If the coin comes up "Heads", it should print to the screen: "List was saved" and return the list intact.
    else:
        print("List was saved")
        return secret_codes
# Hint: Use the random library's choice method to choose an element at random from a sequence.