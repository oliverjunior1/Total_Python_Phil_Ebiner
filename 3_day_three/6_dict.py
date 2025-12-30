my_dictionary = {'c1':'value', 'c2':'value2'}
print(my_dictionary)

result = my_dictionary['c1']
print(result)

customer = {'name': 'John', 'last_name':'Lennon', 'weight':88, 'height':1.76}

query = (customer['last_name'])
print(query)

dic = {1: 55, 2: [10,20,30], 3:{'s1':100, 's2':200}}
print(dic[3]['s2'])

# The question is, how to impress on screen the letter 'a', and put in upper case?
dic = {'k1':['a','b','c'],'k2':['d','e','f']}

print(dic['k1'][0].upper())

dic ={1:'a', 2:'b'}

print(dic)

dic[3] = 'c'
print(dic)

dic[2] = 'b'
print(dic)

print(dic.keys())
print(dic.values())

print(dic.items())