list1 = [1, 5, 10,10, 12, 16, 20]
list2 = [1, 2, 10, 13,13, 16]
list1.extend(list2)
aa=[]
for i in list1:
    if i not in aa:
        aa.append(i)
print(aa)

