#Nested dict designed as dict inside dict 
students={
    "class":{12,11,10,12},
    "subject":{"maths","english","science","maths"},
    "grade":{"A":75,"B":15}

}
print(students)
print(students["class"])
print(students["subject"])
print(students.items())
print(students.keys())
print(students["grade"]["A"])
for key,value in students.items():
    print(key,value)