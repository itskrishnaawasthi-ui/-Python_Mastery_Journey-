#Methods are the functions that belong to objects.

class student:
    collage="shriram collage"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def hello(self):
        print("welcome to the collage:",self.name)
    
    def get_marks(self):
        return self.marks

s=student("keshav",98)
print(student.collage)
s.hello()
print(s.get_marks())        
        