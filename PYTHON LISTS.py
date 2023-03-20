# PYTHON LISTS 
# list is one of the 4 built in datatypes of python.
# lists are used to store collection of data.
# Lists are used to store multiple items in a single variable.
# they are created using square brackets.
basket=["apple", "orange", "cherry"] # list
print(basket) #print the list

# to get length of the list we use len() function 
print(len(basket))

# lists can be of any data type as list of integers, list of boolean, list of srings etc.
list1=[ 1, 3, 5]
list2=[True, True, False]
list3=['one','two','three']

# or a list can store multiple datatypes
list4=[2,True, 6, 'john']

# list items are indexed and we can acceSS them by referring to the index number
print(basket[0]) # to get the first element by positive indexing
print(basket[-1]) # to get the last data using negative indexing
# list is changeable - we can change, add, remove items in a list after it has been created.
basket.append('kiwi')
print(basket)

# to insert a list item at the specific index, we use insert() function
basket.insert(1, 'graps')
print(basket)

# to remove the the topmost element of a list we use pop() function
basket.pop()
print(basket)

# the pop method also removes the specified index
basket.pop(2)
print(basket)

# lists are indexed, lists can have items with the same value

# List Slicing  lst[initial index : end index : index jump]
print(basket[0 : 2 : ])
print(basket[-3 : -1 : ])
print(basket[0 : 3 : 2 ])
print(basket[-2 : -1 : ])

# to clear the list we use clear() function
basket.clear()
print(basket)

# to get the type
print(type(basket))