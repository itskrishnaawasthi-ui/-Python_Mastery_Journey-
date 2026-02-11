arr=[1,2,3,4,5]
print("list before rotationo is;",arr)
pos=int(input("enter the position you want to rotate"))
list=arr[-pos: ]+arr[ :-pos]#---- this set of list slices rotate the list by position given-------- to them
print("list after rotation is:",list)