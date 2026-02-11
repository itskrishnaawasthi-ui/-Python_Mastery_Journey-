#NESTED LIST
matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]


for row in matrix:
  print(row)

list=[[a,b]for a in range(3,6)for b in range (4,8)if a+b==8]
print(list)