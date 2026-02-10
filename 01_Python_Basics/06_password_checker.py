#PASSWORD STENGTH CHECKER
password=input("ENTER THE PASSWORD:")

if len(password)<6:
    print("Weak password(too short)\n")

elif password.isdigit():
    print(" WEAK PASSWORD (ONLY NUMBER):\n")

elif password.isalpha():
    print(" WEAK PASSWORD(ONLY LETTERS):\n")

else:
    print("STRONG PASSWORD:\n")

