import os 
# creating a new file
with open("oscheck.txt","w")as f:
    f.write("hello, this is to check if the file exists or not ")

#checking if file exits.
if os.path.exists("oscheck.txt"):
    print("file exits")

# #Rename the file
# os.rename("oscheck.txt","renamed_os.txt")

# #Delete the file 
os.remove("renamed_os.txt")

#To check current working directory path 
current_path=os.getcwd()
print("Current working Directory:",current_path)
