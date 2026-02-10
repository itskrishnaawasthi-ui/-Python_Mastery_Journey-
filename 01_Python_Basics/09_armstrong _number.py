n=int(input("enter the armstrong number to check"))
store=n
nef=0
while n>0:
    num=n%10
    next=num**3
    nef=nef+next
    n=n//10
    print(nef)
if nef==store:
    print("yes it is a armstrog number")
else:
    print("change the number and run again")

