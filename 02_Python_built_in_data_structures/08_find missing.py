arr=[1,2,4,5,6]
n=6
sum=0
#also to get sum of arr easily we can use = sum(arr)
real_sum= sum(arr)
for i in arr:
    sum=sum+i
    #----formula fro expected sum of natural number is= ( n * (n+1)) // 2
expected_sum=( n * (n+1)) // 2
#also to get sum of arr easily we can use = sum(arr)
real_sum= sum(arr)
print("missing number is:",expected_sum-real_sum)

print("missing number is:",expected_sum-sum)

