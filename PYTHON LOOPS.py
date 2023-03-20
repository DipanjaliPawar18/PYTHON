# PYTHON LOOPS
# it has two primitive loop commands- 
# while loops and for loops
# the while loop- we can execute a set of statements,
# as long as a condition is true
i= 1
while i<=10:
    print(i)
    i += 1

# we can also use the break and continue or if else statements along with loops

# the for loop- we can execte a set of statements, once for each item in a list, tuple etc.
cities=['Bhopal', 'Indore', 'Delhi']
for x in cities:
    print(x)

# loopint through a string
for x in "rabbit":
    print(x)

# the range function
for x in range(5):
    print(x)
for x in range(5, 10):
    print(x)
for x in range(1,10,2):
    print(x)   