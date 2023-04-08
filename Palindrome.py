# Palindrome
# palindrome is a string whose reverse is same as the string itself 
str = input(("enterthe string"))
if(str== str[::-1]):
    print("string is a palindrome")
else:
    print("it is not a palindrome")

# other way
string= input(("enter the string"))
revStr = string[ : :-1]
if (string==revStr):
    print("yes, it's a palindrome")
else:
    print("not a palindrome")


# another way
def palindromeOrNot(s) :
    return s == s[ : : -1]

s= "malayalam"
res = palindromeOrNot(s)

if res :
    print("this is a palindrome")
else :
    print("this is not a palindrome")