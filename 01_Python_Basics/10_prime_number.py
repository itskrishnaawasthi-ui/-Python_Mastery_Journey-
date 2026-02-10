#---To check a prime we check three conditions 1.n<=1--for not prime  2. n==2-- for prime  3.n%2==0--not a prime and rest of all are prime
num=int(input("enter the number:"))
if num<=1:
    print("not a prime:")
elif num==2:
    print("it is a prime")
elif num%2==0:
    print("not a prime")
else:
    print("it is a prime")