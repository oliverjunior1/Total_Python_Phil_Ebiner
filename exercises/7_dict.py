# Update the information in our dictionary called my_dict (reassigning new values to the keys as appropriate), and add a new key called "country". The new data is:
#
# name: Karen
#
# surname: Jurgens
#
# age: 36
#
# occupation: Editor
#
# country: Colombia
#
# to do this, you should not change the line of code already written, but update the values using dictionary methods.

my_dict = {"name":"Karen", "surname":"Jurgens", "age":35, "occupation":"Journalist"}

my_dict['country'] = "Colombia"
my_dict['age'] = 36
my_dict['occupation'] = 'Editor'

print(my_dict)