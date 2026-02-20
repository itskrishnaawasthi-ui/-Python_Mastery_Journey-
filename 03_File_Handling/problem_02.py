#Write a program to read a file and display its contents along with line numbers before each line
f= open('sampletxt.txt','r')
count=1
while True:
    data= f.readline()
    if not data:
        break
    print(f"{count}.{data}",end="")
    count+=1
f.close()


#second approach 
f= open('sampletxt.txt','r') 
count=1
for line in f:
    print(f"{count}.{line}",end="")
    count+=1
f.close()