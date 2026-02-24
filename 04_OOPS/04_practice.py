'''Create student class that takes name and marks of 3 student as argument in constructor .
   Then create a method to print the average.'''

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def average(self):
        sum=0
        for value in self.marks:
            sum+=value
        print(self.name,"your marks are:%.2f"%(sum/3))
        print("{:.2f}".format(sum/3))

s=student("mohan",[99,34,55])       
s.average()

s.name="raghav"
s.average()