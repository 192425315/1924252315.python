num = 123
sum = 0

while num > 0:
    rem = num % 10
    sum += rem  
    num //= 10      

print("Sum of digits is:", sum)
