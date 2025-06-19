a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
d=(b*b-4*a*c)
if(d==0):
    print("same and real roots")
elif(d>0):
    print("different and real roots")
else:
    print("imaginary roots")
