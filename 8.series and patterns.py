n = 5
for i in range(1, n+1):
    print(i, end=' ')
print()
for i in range(1, n+1):
    print(str(i) * i)
for i in range(1, n+1):
    print(' ' * (n - i) + '* ' * i)
