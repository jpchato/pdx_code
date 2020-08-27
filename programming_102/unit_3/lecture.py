employee_availabilities = {} # dictionaries use curly brackets
# print(type(employee_availabilities))

# add key:value pairs
availabilities = {
    'Keegan': 'Mon', 
    'Sarah':'Tues',
}

# keys are passed to dictionaries using square brackets
# dictionary_name[key]
# get the value at the key 'Keegan'
keegan_availability = availabilities['Keegan']
print(keegan_availability) # Mon

sarah_availability = availabilities['Sarah']
print(sarah_availability) # Tues

# Dictionary keys can be strings or integers only

# this is not a list
# dictionary with integers
# using integers as keys can be confusing when referencing values, because the syntax looks like a list
numbers = {
    0: 'zero',
    1: 'one',
    2: 'two'
}
print(numbers[0])

# dictionary values can be any data type, even other dictionaries
availabilities = {
    # key:value,
    'Keegan': ['Mon', 'Tues', 'Wed', 'Thu', 'Fri'], # list as a value
    'Anthony': ['Mon', 'Wed', 'Fri'],
    'Sarah': 'Thu'
}

# since keegan's availability is a list, each item can be referenced with its index
keegan = availabilities['Keegan']
print(keegan[2])

sarah = availabilities['Sarah']

# add a new key:value pair
availabilities['Al'] = 'Fri'
print(availabilities)

# code will break if a non-existent key is referenced
# remove key:value pairs with keyword 'del'
# del dictionary_name['key_to_delete']
del availabilities['Anthony']

print(availabilities)

# Dictionary methods
# dictionary_name.get(key, default_return_value)
# .get() will return the value at the key if it exists
# otherwise, return the default_value

anthony = availabilities.get('Anthony', 'That key doesn\'t exist')
print(anthony)

keegan = availabilities.get('Keegan', 'That key doesn\'t exist')
print(keegan)

# .pop(key) - remove the key:value pair at the key and return the value
removed_value = availabilities.pop('Keegan')
print(removed_value)
print(availabilities)

new_employees = {
    'John': 'Mon',
    'George': 'Tue',
    'Ringo': 'Fri'
}

availabilities.update(new_employees)
print(availabilities)

for name in availabilities:
    print(name)

# line 81 and 86 have the same output
# print(availabilities.keys())
for key in availabilities.keys():
    print(key)

print(availabilities.items())