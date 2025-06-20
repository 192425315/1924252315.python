n = 153
sum = 0
temp = n  
while n > 0:
    rem = n % 10
    sum += rem ** 3
    n //= 10

print(sum)

if sum == temp:
    print("It is an Armstrong number.")
else:
    print("It is not an Armstrong number.")
