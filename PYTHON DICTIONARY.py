# PYTHON DICTIONARY
# dictionaries are used to  store data values in key:value pairs
# a dictionary is a collection of ordered, changeable and do not allow duplication
# dictionaries are written with curly brackets
info={'name':'dipanjali', 'branch': 'ICB', 'scholar no.': 31440}
print(info)

# to access the value the key name is referred
print(info['name'])

# the keys() method will return a list of all the keys in the dictionary
print(info.keys())

# the values() method will return a list of all the values in the dictionary 
print(info.values())

# the update() method will update the dictionary with item
info.update({'branch': 'CSEITCS'}) 
print(info) 

# to add an item to dictionary
info['roll no.'] = 18
print(info)

# to remove the items from a dictionary - pop() method
info.pop('scholar no.')
print(info)

# to clear the dictionary we use clear() method
info.clear()
print(info)

# to get the type
print(type(info))