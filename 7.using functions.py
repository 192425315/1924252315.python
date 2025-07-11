def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def largest(lst):
    return max(lst)

def area_of_circle(radius):
    return 3.1416 * radius * radius

print("Factorial of 5:", factorial(5))
print("Largest number:", largest([1, 5, 8, 3]))
print("Area of circle with radius 3:", area_of_circle(3))
