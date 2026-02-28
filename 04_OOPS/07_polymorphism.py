"""
Demonstrates method overloading (Compile-time polymorphism)
"""
#Using default arguments
class calculator:
    def add(self,a,b,c=0):
        print(f"Addition of number {a},{b},{c} is ",a+b+c)

#Creating Object
calc=calculator()
#Calling Method
calc.add(3,4)
calc.add(3,4,5)

#Using *args
#*args allow you to pass any number of arguments.

class calculator:
    def add (self,*args):
        total=0
        for num in args:
            total+=num
        print("Sum is:",total)

# create object
calc=calculator()
calc.add(3,4)
calc.add(3,4,5)
calc.add(4,5,3,4,2)
    





"""
Demonstrates method overriding (runtime polymorphism)
"""

class Bird:
    def sound(self):
        print("Bird makes a sound")


class Sparrow(Bird):
    def sound(self):
        print("Sparrow chirps")


class Parrot(Bird):
    def sound(self):
        print("Parrot talks")


# Polymorphism in action
birds = [Bird(),Sparrow(), Parrot()]

for bird in birds:
    bird.sound()