#----to string gare nagram if they contain same charecter with the same frequency but possibly in different order ------------
#  i.e listen=silent,  triangle= integral.........
# we can solve it wit two methods 1. with just sorting the both string and makinig them equal  2. to use count charecter the checking to be equal....
str1="listeo"
str2="silent"
if sorted(str1)==sorted(str2):
    print("................Strings are equal and are ANAGRAM...............")
else:
    print("...CHECK for another one...")
    