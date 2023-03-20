# PYTHON LOGICAL STATEMENTS
# python supports the usual logical conditions from mathematics
# equals, not equals, less than, less than or equal to, greater than, greater than or equal to 

# if statement in python
a=3
b=4
if b>a:
    print(" b is greater than a")

# elif in python- it means "if the previous conditions were not true, then try this condition"
x= 4
y= 6
if x>y:
    print("x is greater")
elif x<y:
    print("y is greater")

# else in python- it catches anything which is not caught by the preceding conditions
p=45
q=45
if p>q:
    print("p is greater")
elif p<q:
    print("q is greater")
else:
    print("both are equal")
    