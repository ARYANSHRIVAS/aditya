#Write a Python program to find the maximum among 4 numbers using multiple `if` statements.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a > b and a > c and a > d:
    print("Maximum number is:", a)

if b > a and b > c and b > d:
    print("Maximum number is:", b)

if c > a and c > b and c > d:
    print("Maximum number is:", c)

if d > a and d > b and d > c:
    print("Maximum number is:", d)