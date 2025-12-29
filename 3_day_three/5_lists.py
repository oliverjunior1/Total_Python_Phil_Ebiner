my_list = ['a', 'b', 'c']
my_list_2 = ['d', 'e', 'f']
my_list_3 = my_list + my_list_2

# Show the [start, end] but remember, the end is not included.
result = my_list[0:2]

print(result)
print(my_list_3)

my_list_3[0] = "alpha"
print(my_list_3)

my_list_3.append('g')
print(my_list_3)

my_list_3.pop()
print(my_list_3)

my_list_3.pop(0)
print(my_list_3)

list1 = ['g', 'o', 'b', 'm', 'c']
new_list = list1.sort()
print(new_list)
print(type(new_list))
list1.reverse()
print(list1)
