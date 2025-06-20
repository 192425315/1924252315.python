# Number series: 1 2 3 ... n
n = 5
for i in range(1, n+1):
    print(i, end=' ')
print()

# Number Pattern
for i in range(1, n+1):
    print(str(i) * i)

# Pyramid pattern
for i in range(1, n+1):
    print(' ' * (n - i) + '* ' * i)
