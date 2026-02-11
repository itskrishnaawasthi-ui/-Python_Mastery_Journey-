#List comprehension is a short and clean way to create a new list from an existing list
squares = [x**2 for x in range(1, 6)]

even_numbers = [x for x in range(10) if x % 2 == 0]

words = ["apple", "banana", "cherry"]

upper_words = [word.upper() for word in words]

print(upper_words)

print(squares)

print(even_numbers)
