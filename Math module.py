# Math module
# python has built-in module that can be used for mathematical tasks
# the math module has a set of methods and constants
import math
# the math.degrees() method converts an angle from radians to degrees
d = math.degrees(1.4)
print(d)

# math.factorial method returns the factorial of a number
f = math.factorial(10)
print(f) 

# math.sqrt() method returns square root of a number
sq = math.sqrt(36)
print(sq)

# like this there are many more methods to provide ease to our mathematical calculations

# some constants are also available there
# math.pi returns PI(3.1415...)
from math import pi

def area(r):
    area= pi * r * r
    return area

a = area(4)

print("area of the circle is", a)