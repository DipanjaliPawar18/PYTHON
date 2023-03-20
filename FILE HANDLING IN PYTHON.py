# FILE HANDLING IN PYTHON
# the key function for working with files in python is open() function
# the open() function takes two parameters as filename and mode
# there are  different modes
# 1.read "r"-opens file for reading
# 2. write "w"- opens file for writing, creates file if doesn't exist
# 3. append "a"- opens file for appending, also creates if doesn't exist
# 4. create "x"- creates the specified file

#READ MODE-
f= open("demofile.txt", "r")
# read() method is used for reading the content of file
print(f.read())

# to read only parts of a file
f= open("demofile.txt", "r")
print(f.read(5))

# we can read one line using readline() method
f= open("demofile.txt", "r")
print(f.readline())

#WRITE MODE-
f= open("demofile.txt", "a")  #appending the file
f.write("more content added to this file")
f.close()
#open and read the file
f= open("demofile.txt","r")
print(f.read())

# to overwrite the content
f= open("demofile.txt", "w")
f.write("the previous content is deleted now!!!")
f.close()
# open and read the file
f= open("demofile.txt", "r")
print(f.read())

# to create a new file
f= open("newfile.txt","x")

# add content to the previously created newfile
f= open("newfile.txt", "a")
f.write("hey!!! this is new file")
f.close()

# to read the new file
f= open("newfile.txt", "r")
print(f.read())