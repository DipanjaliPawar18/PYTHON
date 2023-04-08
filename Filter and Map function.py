# Filter and Map function 

# python filter() function
""" the filter() function returns an iterator
where the items are filtered through a function to test 
if the item is accepted or not"""
# SYNTAX: filter(function, iterable)
# function - a function to be run for each item in the iterable
# iterable - the iterable to be filtered
ages = [2, 5, 12, 18, 20, 23, 25, 28]

def func(x):
    if x < 18:
        return False
    else:
        return True
adults = filter(func, ages)
for x in range adults:
    print(x) 

"""map function in python
returns a list of the results after applying the given function
to each item of a given iterable (list, tuple etc.)"""

def add(n):
    return n + n
numbers = (1, 2, 3, 4, 5)
result = map (add, numbers)
print(list(result))

# lambda expression with map() function
result= map(lambda x: x * 2, numbers)
print(list(result))