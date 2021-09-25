a=int(input("enter ur number:- "))
b=a
d_sum=0
while a:
    d_sum+=a%10
    a//=10
if b%d_sum==0:
    print("its a harsad number")
else:
    print("its not a harsad number ")


