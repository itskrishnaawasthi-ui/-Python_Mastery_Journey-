student={"shyam":20,"ram":30,"hari":40}
print(student.keys())# print all keys
print(student.values())# print all values

for key in student.keys():
    print(key)
for value in student.values():
    print(value)
print(student.items()) 
print(student.get("shyam")) # print value of the key

