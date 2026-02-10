import random

num=random.randint(1,10)
print("Guess a number between 1 to 10:")

while True:
  guess=int(input("Enter your Guess:"))
  
  if guess==num:
    print("Correct! you guessed it right:")
    break
  elif guess<num:
    print("TOO LOW!")
  else:
    print("TOO HIGH!")
