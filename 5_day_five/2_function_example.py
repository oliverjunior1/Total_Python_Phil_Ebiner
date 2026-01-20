coffee_pricees = [('capuccino', 1.5),
                  ('espresso', 1.2),
                  ('mocha',1.9)]

def most_expensive_coffee(list_of_prices):

    hightest_price = 0
    my_most_expensive_coffee = ''

    for coffee, price in list_of_prices:
        if price > hightest_price:
            hightest_price = price
            my_most_expensive_coffee = coffee
        else:
            pass

    return (my_most_expensive_coffee, hightest_price)

print(most_expensive_coffee(coffee_pricees))