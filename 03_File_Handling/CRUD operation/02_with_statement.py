with open("message2","w")as f: # open file for writing
 tup=(12,23,212,"Make it")
 lis=["stored data",12,56,33,444,22,12]
 di={1:"mohan",2:"ram"}
 f.write(str(tup)) # it only except data in string format to convert all data type to string first
 f.write(str(lis))
 f.write(str(di))

 
f=open("message2","r") # open file for reading
data=f.read()
print(data)


with open("message","w") as f:
    message1="never to let down yourself try try and try fail fail fail but one day you will win "
    data=f.write(message1)
    print(f.seek(0))
    print(data)
