# INPUT= [1,2,3],[2,3,4]
# OUTPUT=[1,4]
a=set([1,2,3])
b=set([2,3,4])
result=a.symmetric_difference(b)
print(list(result))