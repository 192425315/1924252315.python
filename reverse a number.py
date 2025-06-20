number=1234
reverse=0
while number>0:
    rem=number%10
    reverse=reverse*10+rem
    number//=10
print(reverse)
