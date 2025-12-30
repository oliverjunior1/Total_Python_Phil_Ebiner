# Remember that, set can't have repetition.
my_set = set([1,2,3,4,5,1,1,2,2,2])
print(type(my_set))
print(my_set)
# Set can't support some tuple, our another object, only tuple. like this {1,2,(3,4),5} is True, but not another way

other_set = {1,2,3}
print(type(other_set))
print(other_set)

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2, s1)
print(s3)

another_set = {1,2,3}
another_set.add(2)
print(another_set)
another_set.add(4)
print(another_set)
another_set.remove(3)
print(another_set)
draw = another_set.pop()
print(draw)


