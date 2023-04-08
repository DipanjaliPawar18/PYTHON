# Calculator
a = input("enter first number:")
b = input("enter second number:")
ch = input(int("enter the choice:"))
if ch==1 :
    print(a+b)
elif ch==2 :
    print(a-b)
elif ch==3 :
    print(a*b)
elif ch==4 :
    print(a/b)
elif ch==5 :
    print(a%b)
else :
    print("incorrect choice")