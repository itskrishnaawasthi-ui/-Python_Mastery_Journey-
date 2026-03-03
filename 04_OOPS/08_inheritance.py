'''Technique of creating a new class from an existing class is called inheritence.
old class-- base class
new class--derived class '''

#Program ato demonstrate use of inheritance.
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)

class teacher:
    def __init__(self,name,age,exp,region):
        person.__init__(self,name,age)
        self.exp=exp
        self.region=region
    def display(self):
        person.display(self)
        print("Year Experience:",self.exp)
        print("Region:",self.region)


print("#### DETAIL ABOUT TEACHERS ####")
t=teacher("Jaya",24,"4 year","UP")
t.display()




"""
Demonstrates single inheritance
"""

class Animal:
    def speak(self):
        print("Animal makes a sound")


# Child class inheriting from Animal
class Dog(Animal):
    def bark(self):
        print("Dog barks")


dog = Dog()

dog.speak()  # Inherited method
dog.bark()   # Own method
          
            