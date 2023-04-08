# Making tuple mutable

# changing an element
fruits = ("apple", "mango", "graps")
lst = list(fruits)
lst[0] = "kiwi"
fruits = tuple(lst)

print(fruits)

# adding element to the tuple 
tup = (2, 4, 6, 8)
t = list(tup)
t.append(10)
tup = tuple(t)

print(tup)

# remove elements from the tuple
cities=("indore","bhopal","delhi","mumbai")
t= list(cities)
t.remove("indore")
cities = tuple(t)

print(cities)