#FUNCTIONS
def greet(name):
    print("hello world")

def Sum(num1,num2):
    return num1+num2

greet("xavier")
result=Sum(1,4)
print("SUM of the numbers:",result)

#---lambda function -----
# also called anonymous functions or inline functions ----
# it takes any number but can return only one value .. 
# Syntex:  lambda expression:expression
print((lambda n: n*n*n)(3))
print((lambda x,y,z: (x+y+z)/3)(10,20,30))
r=lambda x:x.upper()
print(r("mohali"))
#---- Namespaces_----------
#global(),local()
#outer function 
def fun():   # globall ()
    a=10    
    print("use pie and say hurray")
    def display():   # local()
        print("born with pride so live with it")
        print(a)    
    display()
fun()

# for local and global variable----
# use keywords locals(),globals()
# To prove "a" in local and global function are different----
def dev():
    a=12
    print(a)
    print(id(a))

    def devi():
      b=13
      print(b)
      print(id(b))

    devi()


dev()






