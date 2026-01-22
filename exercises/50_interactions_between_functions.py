# Create a function called reduce_list() that takes a list (numbers) as an argument, and returns also a list, but
# duplicates (leaving only one of the numbers if there are duplicates) and removing the highest value. The order of the
# elements can be changed.
def reduce_list(numbers):
    reduce_set = sorted(set(numbers))
    numbers_reduced = list(reduce_set)
    numbers_reduced.pop()
    return numbers_reduced
numbers = [1,2,15,7,2]
# For example, if given the list [1,2,15,7,2] it should return [1,2,7].
# Create a function called average() that can receive as an argument the list returned by the previous function, and
# that calculates the average of its values. It should return the result (a float), without printing it.
values = reduce_list(numbers)

def average(values):
    return float(sum(values)/len(values))

print(average(values))

