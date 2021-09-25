string_list = ["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"]
l=[]
for i in string_list:
    if i not in l:
        l.append(i)
print(l)