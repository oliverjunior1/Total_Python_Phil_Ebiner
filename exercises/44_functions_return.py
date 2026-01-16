# Create a function called usd_to_eur that takes a numeric value (an amount in US dollars) as its only parameter, and
# returns the equivalent amount in euros as a result. For the purposes of this example, we will take the conversion
# 1 USD = 0.90 EUR.
def usd_to_eur(usd):
    return usd*0.9
# Create a variable called dollars and store any amount in it. Then, pass it to your function and evaluate its result.
dollars = usd_to_eur(10)
# Hint: to perform the conversion, the function internally must multiply this value in dollars by 0.90 to obtain the
# equivalent amount in euros.

print(dollars)