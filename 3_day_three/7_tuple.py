my_tuple = (1,2,(10,20),3,4)
my_tuple = list(my_tuple)
print(type(my_tuple))
my_tuple = tuple(my_tuple)

t = (1,2,3)
x, y, z = t
print(my_tuple[-2])
print(my_tuple[2][0])
print(type(my_tuple))

print(x, y, z)
print(len(t))
print(t)
print(t.count(1))
print(t.index(2))
