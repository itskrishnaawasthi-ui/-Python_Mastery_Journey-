#-------to count frequency of a number----------------
arr=[20,29,29,23,23,14,14]
freq={}
for num in arr:
   freq[num]=freq.get(num,0)+1
print(freq)

