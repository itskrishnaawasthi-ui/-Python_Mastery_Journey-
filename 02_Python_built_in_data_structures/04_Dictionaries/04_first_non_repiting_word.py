str="a lone wolf is more dangerous then a group of dogs"
req={}
for word in str:
    req[word]=req.get(word,0)+1

for word in str:
   if req[word]==1:
    print("the word is :",word)
    break




