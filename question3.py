l,u,p,d=0,0,0,0
user=input("Please! enter your password:-  ")
for i in user:
    if i.islower():
        l+=1
    if i.isupper():
        u+=1
    if i.isdigit():
        d+=1
    if i=="@" :
        p+=1
if l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(user):
    print("its a strong password")
else:
    print("weak password")
