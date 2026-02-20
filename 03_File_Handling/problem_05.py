#Checking for even odd in a Comma-Separated File 
with open("number","w") as f:
    f.write("12,3,12,445,232,1212,443,435,423,232,32223")

with open("number","r") as f:
    data=f.read()
    print("Original data:\n",data)
    new_data=data.split(",")
    Count=0
    Even_no=0
    Length=len(new_data)
    for num in new_data:
        if int(num)%2==0:
            Count+=1
            Even_no+=1
            print(f"{Count}  Even Number:")

        else:
            Count+=1
            print(f"{Count}  Odd Number:")
    Odd_no=Length-Even_no
    print("Total number of elements :",Length)
    print("Total Even numbers are:",Even_no)
    print("Total Odd numbers are:",Odd_no)
            