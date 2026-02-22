'''
   Constructor--
                In python classes have a function which always executed when the class is being initiated.
'''

class car:
    def __init__(self,model,manufacture): #self parameter is a reference to the current instance of the class,used to access the variables that belongs to the class.
        self.model=model 
        self.manufacture=manufacture
        print("Car with it's manufactured year")

s1=car("Tesla",2000)

s2=car("Tata",2010)
print(s2.model)
print(s1.manufacture)