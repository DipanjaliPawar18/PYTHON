# os and sys module
"""the os module in Python provides functions for interacting with the operating system.
OS comes under Python's standard utility modules. 
this module provides a portable way of using operating system-dependent functionality""" 

# getting the current working directory

import os

cmd = os.getcwd()

print("current working directory:", cmd)

# listing out files and directories with python
import os
path = "/"
d_list = os.listdir(path)

print("files and directories in", path ,  " :")
print(d_list)

# getting name of os
import os
print(os.name)

# os.access() method
# syntax os.access(path, mode)

import os
import sys

# checking if the file exists or not
p1 = os.access("demofile.txt", os.F_OK)
print("exists the path:", p1)

# checking if the file is readable or not
p2 = os.access("demofile.txt", os.R_OK)
print("access to read the file:", p2)

# checking access with os.W_OK
p3 = os.access("demofile.txt", os.W_OK)
print("access to write in the file:",p3)

# checking access with os.X_OK
p4 = os.access("demofile.txt", os.X_OK)
print("check if path can be executed:", p4)


""" the sys module provides various functions and variables that are used
to manipulate different parts of the python runtime environment"""

import sys

print(sys.version)

# stdout

import sys
sys.stdout.write("hello world!!!")