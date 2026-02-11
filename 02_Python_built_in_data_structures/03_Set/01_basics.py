#set is created using curly braces {}
#Sets are unique,unordered and mutable (can be changed after creation)
data=set("hello")
print(data)
numbers={12,12,34,56,78,90}
print(numbers)
#Adding element to set
numbers.add(100)    
print(numbers)
#Adding duplicate element to set
numbers.add(34)
print(numbers)
#Removing element from set
numbers.remove(56)
print(numbers)

