#Write a program to read the contents of the file "message" one charecter at a time. Print each charecter that is read.
with open("sampletxt.txt","r") as f:
 while True:
  data=f.read(1)
  if data=="":
   break
  print(data)
  
  