# Write a function that requires an indefinite number of
# arguments. What this function must dois return True if at any
# time the number zero has been entered twice consecutively.
#
# For example:
# (5,6,1,0,0,9,3,5)>>>True
# (6,0,5,1,0,3,0,1)>>>False

# def has_double_zeros(*args):
#     for i in range(len(args) -1):
#         if args[i] == 0 and args[i + 1] ==0:
#             return False
#     return False
#
# print(has_double_zeros(5,6,1,0,0,9,3,5))
# print(has_double_zeros(6,0,5,1,0,3,0,1))

def has_double_zero(*args):
    return any(a == 0 and b == 0 for a, b in zip(args, args[1:]))

print(has_double_zero(5,6,1,0,0,9,3,5))
print(has_double_zero(6,0,5,1,0,3,0,1))





