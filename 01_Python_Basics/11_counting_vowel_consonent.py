vowels="aeiou"
str="name the person2 and rest well"
vowel=0
for i in str:
    for j in vowels:
        if i==j:
            vowel+=1
print("vowels in string are:",vowel)
   
new=len(str)-vowel
print("consonent in str are:",new)

#----------------Second approach-------------------

vowels="aeiou"
str="name the person and rest well"
vowel=consonent=0
for i in str:
        if i in vowels:
             vowel+=1
        else:
             consonent+=1
print("vowwls are:",vowel,"consonents are:",consonent)