# Lambda function
# a lambda function is a small anonymous function
# a lambda function can take any number of arguments,
# but can only have one expression.
# SYNTAX: lambda argumnts : expression

# with one argument 
x= lambda a : a + 12
print(x(8))

# with two arguments
x = lambda a, b : a-b
print(x(5,8))

# with three arguments
x = lambda a, b, c : a * b + c
print(x(8,6,2))

# generally lambda function is used as anonymous function inside a function
def thisFunc(n):
    return lambda a : a * n

doubleThis = thisFunc(2)
tripleThis = thisFunc(3)

print(doubleThis(45))
print(tripleThis(50))