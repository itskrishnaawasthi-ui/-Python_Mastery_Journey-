# #To delete a file from the system.
# import os
# os.remove("sample.text") # os uses remove( ) to delete the file

# #To clear all content (without deleting the file)
# open("data","w").close() # this will empty the file but keep it.
# #OR
# with open("data","w"):
#     pass

#To delete a specific line
with open("source","w")as f:
    f.write("how have you been\n")
    f.write("hello!\n")
    f.write("how have you been")
    f.write("i am fine")

with open("source","r") as f:
    lines=f.readlines()

with open("source","w") as f: 
    for line in lines:
        if line!="how have you been":
          f.write(line)