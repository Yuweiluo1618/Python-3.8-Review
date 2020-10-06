list1 = []
for i in range(1,3):
   for j in range(3):
       tuple1 = (i, j)
       list1.append(tuple1)

print(list1)

list2 = [(i, j)for i in range(1, 3) for j in range(3)]
print(list2)

