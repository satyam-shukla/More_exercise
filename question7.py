list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1]
aa=[]
for i in list1:
    if i in list2:
        aa.append(i)
print(aa)
