a=int(input("enter the value:"))
b=int(input("enter the value:"))
c=int(input("enter the value:"))
if(a>b):
    if(a>c):
        print("greatest:",a)
    else:
        print("greatest:",c)
else:
    if(b>c):
        print("greatest:",b)
    else:
        print("greatest:",c)
