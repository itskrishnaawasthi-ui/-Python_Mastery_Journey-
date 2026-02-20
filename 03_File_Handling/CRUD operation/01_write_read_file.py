#  w- write mode, r- read mode, a- append mode ,r+ - reading and writing , w+ - writing and reading , a+ -appending and reading
msg1="hello !\n"
msg2="how have you been\n"
msg3="Are you fine !\n"
msg4="if yes say-will... else say-never  "
f=open("message","w") # open file for writing
f.write(msg1)
f.write(msg2)
f.write(msg3)
f.write(msg4)
f=open("message","r") # open file for reading
data=f.read()
print(data) 
f.close() # close the file after use

# there are two more methods to read the file
f=open("message","r")
data=f.read() # read the first line of the file
print(data)
data=f.readline() # read the second line of the file
print(data)
data=f.readlines() # read the remaining lines of the file and store in a list
print(data)


# there are more method in write mode
f=open("message","w")
f.writelines([msg1,msg2,msg3,msg4]) # write a list of strings to the file
f.close()   

