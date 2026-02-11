arr=[1,2,4,5,0,6,7]
non_zeroes=[]
for i in arr:
  if i!=0:
    non_zeroes.append(i)
zeroes=len(arr)-len(non_zeroes)
print("count of  zero  is:",zeroes)
non_zeroes+=[0]*zeroes
print(non_zeroes)

