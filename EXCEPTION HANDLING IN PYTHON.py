# EXCEPTION HANDLING IN PYTHON
# wwhen an error (exception) occurs, python stop and generate an error message.
# these exception can be handled 
# TRY block- the try block will generate an exception, because x is not defined
try:          # it tests a block of code for errors.
    print(x)
except:       # it lets us handle the error.
    print("x is not defined")
# here if we didn't used the try block, an errorwill be generated and the execution will stop

# the else block lets us execute code when there is no error.
try:
    print("hello")
except:
    print("something went wrong")
else:
    print("nothing went wrong")

# the finally block lets us execute code, regardless of the result of the try and except blocks.
try:
    print(a)
except:
    print("something went wrong")
finally:
    print("the 'try except' is finished")